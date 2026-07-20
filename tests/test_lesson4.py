# CREATE USER
def test_create_user(api_context):
    payload = {"name": "Bagish", "job": "Senior Manager"}
    response = api_context.post("users/4", data=payload)
    print(response.status)
    assert response.status == 201
    body = response.json()
    assert body["name"] == "Bagish"
    print(body)
    assert "id" in body
    assert "createdAt" in body

    #GET USER
def test_get_single_user(api_context):
    response = api_context.get("users/4")
    print(response.status)
    assert response.status == 200

    body = response.json()
    assert body["data"]["id"] == 4
    assert body["data"]["email"] is not None

    #UPDATE USER
def test_update_user(api_context):
    response = api_context.put("users/4", data={"name": "Sood"})
    assert response.status == 200
    assert response.json()["name"] == "Sood"

    #DELETE USER
def test_delete_user(api_context):  
    response = api_context.delete("users/4")
    assert response.status == 204