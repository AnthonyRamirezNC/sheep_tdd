from fastapi.testclient import TestClient
from main import app
from models.models import Sheep

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

def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    data = Sheep(id=7, name="babydoll", breed="Gotland", sex="ewe")

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=data.dict())

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == data.dict()

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    # Include an assert statement to see if the new sheep data can be retrieved.
    get_response = client.get(f"/sheep/{data.id}")
    assert get_response.status_code == 200
    assert get_response.json() == data.dict()


from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test creating a new sheep
def test_add_sheep():
    response = client.post("/sheep/", json={"id": 1, "name": "Dolly", "age": 5})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Dolly", "age": 5}

# Test reading all sheep
def test_get_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test updating a sheep
def test_update_sheep():
    response = client.put("/sheep/1", json={"id": 1, "name": "Updated Dolly", "age": 6})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Dolly", "age": 6}

# Test deleting a sheep
def test_delete_sheep():
    response = client.delete("/sheep/1")
    assert response.status_code == 204
    # Verify the sheep was deleted
    response = client.get("/sheep/")
    assert all(sheep["id"] != 1 for sheep in response.json())

