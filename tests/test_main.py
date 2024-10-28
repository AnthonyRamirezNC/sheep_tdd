from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    #send  get request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    #Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    #Assert that the response JSON matches the expected data
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }