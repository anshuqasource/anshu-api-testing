def test_create_user(api_context):
    payload = {"name": "Anshu", "job": "QA Manager"}
    response = api_context.post("users/", data=payload)
    print(response.status)
    assert response.status == 201
    body = response.json()
    assert body["name"] == "Anshu"
    print(body)
    assert "id" in body
    assert "createdAt" in body