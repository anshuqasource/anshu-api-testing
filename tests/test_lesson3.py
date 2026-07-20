def test_update_user(api_context):
    response = api_context.put("users/2", data={"job": "Director QA"})
    assert response.status == 200
    assert response.json()["job"] == "Director QA"

def test_delete_user(api_context):
    response = api_context.delete("users/2")
    assert response.status == 204