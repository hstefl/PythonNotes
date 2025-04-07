import subprocess
import time

import pytest
import requests
import json


@pytest.fixture
def api():
    process = subprocess.Popen(["python", "-m", "main"])
    base_url = "http://127.0.0.1:8000/"
    wait_api_started(base_url)
    yield {'base_url': base_url}

    process.terminate()


def wait_api_started(server_url):
    for _ in range(20):  # Retry for 20 attempts
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                print("Server is fully started!")
                break
        except requests.exceptions.ConnectionError:
            pass  # Server not up yet

        time.sleep(0.5)  # Wait before retrying

    print("Process started but may still be initializing.")


def test_server_responsible(api):
    resp = requests.get(api['base_url'])
    print(resp.json())
    assert resp.status_code == 200


def test_get_users_no_auth(api):
    resp = requests.get(api['base_url'] + "/users")
    assert resp.status_code == 401


def test_get_users_with_auth(api):
    resp = requests.post(api['base_url'] + "token", headers={"X-API-KEY": "app1-secret-key"})
    token = resp.json().get("access_token")
    resp = requests.get(api['base_url'] + "users", headers={"Authorization": f"bearer {token}"})
    assert resp.status_code == 200
    users = resp.json()
    assert len(users) == 2
    assert [user for user in users if "Doe" in user["name"]]


def test_get_users_expired_token(api):
    resp = requests.post(api['base_url'] + "token", headers={"X-API-KEY": "app1-secret-key"})
    token = resp.json().get("access_token")
    time.sleep(5)
    resp = requests.get(api['base_url'] + "users", headers={"Authorization": f"bearer {token}"})
    assert resp.status_code == 401
    assert resp.json().get("detail") == 'Token expired'


def test_create_user(api):
    resp = requests.post(api['base_url'] + "token", headers={"X-API-KEY": "app1-secret-key"})
    token = resp.json().get("access_token")
    user = {"id": 3, "name": "Jan Stefl", "email": "jan@stefl.cz"}
    resp = requests.post(url=api['base_url'] + "users",
                         headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
                         json=user)
    assert resp.status_code == 200
    assert resp.json().get("id") == 3

    resp = requests.get(api['base_url'] + "users", headers={"Authorization": f"bearer {token}"})
    assert resp.status_code == 200
    users = resp.json()
    assert len(users) == 3
