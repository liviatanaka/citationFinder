from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_yields_10_results():
    response = client.get("/query?query=artifical intelligence")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) == 10
    assert json_response["message"] == "OK"

def test_query_yields_few_results():
    response = client.get("/query?query=nlp")
    json_response = response.json()
    assert response.status_code == 200
    assert 1 < len(json_response["results"]) < 10
    assert json_response["message"] == "OK"

def test_query_yields_non_obvious_results():
    response = client.get("/query?query=wolf")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) > 0
    assert json_response["message"] == "OK"
