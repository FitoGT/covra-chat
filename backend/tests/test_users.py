def test_get_users_requires_auth(client):
    response = client.get("/users/")
    assert response.status_code == 403


def test_get_users_with_token(client, registered_user):
    login = client.post("/auth/login", json={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(user["email"] == registered_user["email"]
               for user in response.json())
