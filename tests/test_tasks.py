# ============================================================
# Casos de prueba para la obtención de tareas
# ============================================================

def test_get_tasks(client, auth_headers):

    response = client.get(
        "/tasks",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)


def test_get_task(client, auth_headers):

    response = client.get(
        "/tasks/1",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_get_task_not_found(client, auth_headers):

    response = client.get(
        "/tasks/999999",
        headers=auth_headers
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"


# ============================================================
# Casos de prueba para la creación de tareas
# ============================================================

def test_create_task(client, auth_headers):

    response = client.post(
        "/tasks",
        json={
            "title": "Tarea creada desde Pytest",
            "completed": False
        },
        headers=auth_headers
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Tarea creada desde Pytest"
    assert data["completed"] is False
    assert "id" in data


def test_create_task_without_title(client, auth_headers):

    response = client.post(
        "/tasks",
        json={
            "completed": False
        },
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'title' es obligatorio"


def test_create_task_with_empty_title(client, auth_headers):

    response = client.post(
        "/tasks",
        json={
            "title": "",
            "completed": False
        },
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'title' es obligatorio"


def test_create_task_with_invalid_completed(client, auth_headers):

    response = client.post(
        "/tasks",
        json={
            "title": "Tarea invalida",
            "completed": "false"
        },
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'completed' debe ser un booleano"


# ============================================================
# Casos de prueba para la actualización de tareas
# ============================================================

def test_update_task_title(client, auth_headers):

    response = client.patch(
        "/tasks/1",
        json={
            "title": "Título actualizado"
        },
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["title"] == "Título actualizado"


def test_update_task_completed(client, auth_headers):

    response = client.patch(
        "/tasks/1",
        json={
            "completed": True
        },
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["completed"] is True


def test_update_task_with_empty_title(client, auth_headers):

    response = client.patch(
        "/tasks/1",
        json={
            "title": ""
        },
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'title' debe ser un texto no vacío"


def test_update_task_with_invalid_completed(client, auth_headers):

    response = client.patch(
        "/tasks/1",
        json={
            "completed": "true"
        },
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'completed' debe ser un booleano"


def test_update_task_not_found(client, auth_headers):

    response = client.patch(
        "/tasks/999999",
        json={
            "title": "Tarea inexistente"
        },
        headers=auth_headers
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"


# ============================================================
# Casos de prueba para la eliminación de tareas
# ============================================================

def test_delete_task(client, auth_headers):

    response = client.delete(
        "/tasks/1",
        headers=auth_headers
    )

    assert response.status_code == 204


def test_delete_task_not_found(client, auth_headers):

    response = client.delete(
        "/tasks/999999",
        headers=auth_headers
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"


# ============================================================
# Casos de prueba para cuerpo inválido
# ============================================================

def test_create_task_with_invalid_body(client, auth_headers):

    response = client.post(
        "/tasks",
        json=[],
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"


def test_update_task_with_invalid_body(client, auth_headers):

    response = client.patch(
        "/tasks/1",
        json=[],
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"


# ============================================================
# Casos de prueba para rutas no encontradas
# ============================================================

def test_route_not_found(client):

    response = client.get(
        "/ruta-que-no-existe"
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Recurso no encontrado"


def test_method_not_allowed(client, auth_headers):

    response = client.post(
        "/tasks/1",
        headers=auth_headers
    )

    assert response.status_code == 405

    data = response.get_json()

    assert data["error"] == "Método no permitido"


def test_internal_server_error(client):

    app = client.application

    app.config["PROPAGATE_EXCEPTIONS"] = False

    @app.route("/trigger-500-test")
    def trigger_500_test():
        raise Exception("Error de prueba")

    response = client.get(
        "/trigger-500-test"
    )

    assert response.status_code == 500

    data = response.get_json()

    assert data["error"] == "Error interno del servidor"