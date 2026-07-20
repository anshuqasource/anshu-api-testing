import clients

def test_get_single_user(client):
    
        response = client.get("users/2")
        print(response.status)
        assert response.status == 200

        body = response.json()
        assert body["data"]["id"] == 2
        assert body["data"]["email"] is not None

    