def test_login_and_use_token(api_context):
    login_response = api_context.post("login/", data={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    print(login_response.status)
    assert login_response.status == 200
    token = login_response.json()["token"]

    authenticated_response = api_context.get("users/2", headers={
        "Authorization": f"Bearer {token}"
    })
    assert authenticated_response.status == 200

def test_login_missing_password(api_context):
    response = api_context.post("login/", data={"email": "eve.holt@reqres.in"})
    assert response.status == 400
    assert response.json()["error"] == "Missing password"