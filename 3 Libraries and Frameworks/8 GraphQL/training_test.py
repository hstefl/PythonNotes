import subprocess
import time

import pytest
import requests

DEFAULT_USERS_COUNT = 3


@pytest.fixture
def api():
    """
    This is set up/teardown method per test.
    Database in training is in memory - each test will have fresh default DB data
    """
    process = subprocess.Popen(["python", "-m", "training"])
    graphql_url = "http://127.0.0.1:8000/graphql"
    wait_api_started(graphql_url)
    yield {'graphql_url': graphql_url}

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
    resp = requests.get(api['graphql_url'])
    assert resp.status_code == 200


def test_get_all_users(api):
    assert_users_total(api, DEFAULT_USERS_COUNT)


def test_add_user(api):
    query = """
        mutation {
            addUser(id:100, name:"Jan Stefl", email:"jan@stefl") {
                id
                name
                email
            }
        }
        """
    response = requests.post(api["graphql_url"], json={"query": query})

    assert response.status_code == 200
    assert_users_total(api, DEFAULT_USERS_COUNT + 1)


def assert_users_total(api, total):
    query = """
        query {
            getUsers {
                id
                name
                email
            }
        }
        """
    response = requests.post(api["graphql_url"], json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]['getUsers']) == total
