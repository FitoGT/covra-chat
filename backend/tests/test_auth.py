def test_login_user(client, registered_user):
    response = client.post("/auth/login", json={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
