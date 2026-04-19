import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_shorten_success():
    client = app.test_client()
    res = client.post("/shorten", json={"url": "http://google.com"})
    assert res.status_code == 200

def test_shorten_invalid():
    client = app.test_client()
    res = client.post("/shorten", json={"url": "invalid"})
    assert res.status_code == 400

def test_redirect_not_found():
    client = app.test_client()
    res = client.get("/abc123")
    assert res.status_code == 404

def test_list_urls():
    client = app.test_client()
    res = client.get("/urls")
    assert res.status_code == 200