import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_test_endpoint(client):
    response = client.get('/test')
    assert response.status_code == 200
    assert response.json == {"message": "Cloudfresh test task"}
