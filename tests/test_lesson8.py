def test_create_user_via_client(client):
    response = client.create_user("Anshu", "QA Leader")
    assert response.status == 201