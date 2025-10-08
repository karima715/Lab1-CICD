from app import app

def test_homepage():
    # Use Flask test client
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data
