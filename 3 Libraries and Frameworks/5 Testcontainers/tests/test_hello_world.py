import pytest
from testcontainers.core.container import DockerContainer
import requests


@pytest.fixture(scope='module')
def custom_flask_container():
    with DockerContainer("my-custom-flask-image:latest") as container:
        container.with_exposed_ports(5000)
        container.start()
        yield container


def test_custom_flask_app(custom_flask_container):
    port = custom_flask_container.get_exposed_port(5000)
    response = requests.get(f'http://localhost:{port}/')
    assert response.status_code == 200
    assert response.text == 'Welcome to the Custom 6 Flask Application'
