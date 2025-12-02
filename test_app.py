"""Tests for Flask demo application."""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_healthz_returns_200(client):
    """Test that healthz endpoint returns HTTP 200 status code."""
    response = client.get('/healthz')
    assert response.status_code == 200


def test_healthz_returns_healthy_status(client):
    """Test that healthz endpoint returns healthy status in response."""
    response = client.get('/healthz')
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'message' in data


def test_healthz_returns_json(client):
    """Test that healthz endpoint returns JSON content type."""
    response = client.get('/healthz')
    assert response.content_type == 'application/json'


def test_index_returns_200(client):
    """Test that index endpoint returns HTTP 200 status code."""
    response = client.get('/')
    assert response.status_code == 200


def test_index_returns_welcome_message(client):
    """Test that index endpoint returns welcome message."""
    response = client.get('/')
    data = response.get_json()
    assert 'message' in data
