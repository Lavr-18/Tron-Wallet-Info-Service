
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_wallet_info_post():
    response = client.post("/wallet-info/", json={"address": "TLa6n6KbtqVvfTjHbg76vX91XYmK6Mok2X"})
    assert response.status_code == 200
    assert "address" in response.json()
    assert "trx_balance" in response.json()

def test_get_wallet_info_list():
    response = client.get("/wallet-info/?skip=0&limit=2")
    assert response.status_code == 200
    assert len(response.json()) > 0
