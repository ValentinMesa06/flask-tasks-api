# Casos de prueba para el registro de usuarios
def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "nuevo_usuario",
            "password": "password123"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["username"] == "nuevo_usuario"
    assert "id" in data
    assert "password" not in data
    assert "password_hash" not in data


def test_register_user_with_invalid_body(client):
    response = client.post(
        "/auth/register",
        json=[]
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"


def test_register_user_without_username(client):
    response = client.post(
        "/auth/register",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'username' es obligatorio"


def test_register_user_with_empty_username(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "",
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_register_user_without_password(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "usuario"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'password' es obligatorio"


def test_register_user_with_empty_password(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "usuario",
            "password": ""
        }
    )

    assert response.status_code == 400


def test_register_existing_user(client):
    client.post(
        "/auth/register",
        json={
            "username": "usuario_existente",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "usuario_existente",
            "password": "otra_password"
        }
    )

    assert response.status_code == 409

    data = response.get_json()

    assert data["error"] == "El usuario ya existe"


# Casos de usa para el login del usuario
def test_login_user(client):
    client.post(
        "/auth/register",
        json={
            "username": "usuario_login",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_login",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "access_token" in data
    assert isinstance(data["access_token"], str)


def test_login_with_invalid_body(client):
    response = client.post(
        "/auth/login",
        json=[]
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"


def test_login_without_username(client):
    response = client.post(
        "/auth/login",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'username' es obligatorio"


def test_login_with_empty_username(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "",
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_login_without_password(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_login"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'password' es obligatorio"


def test_login_with_empty_password(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_login",
            "password": ""
        }
    )

    assert response.status_code == 400


def test_login_with_nonexistent_user(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_inexistente",
            "password": "password123"
        }
    )

    assert response.status_code == 401

    data = response.get_json()

    assert data["error"] == "Usuario o contraseña incorrectos"


def test_login_with_incorrect_password(client):
    client.post(
        "/auth/register",
        json={
            "username": "usuario_login",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_login",
            "password": "password_incorrecta"
        }
    )

    assert response.status_code == 401

    data = response.get_json()

    assert data["error"] == "Usuario o contraseña incorrectos"