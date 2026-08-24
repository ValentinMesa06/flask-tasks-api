# Casos de prueba para la obtención de tareas
def test_get_tasks(client):

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)


def test_get_task(client):

    response = client.get("/tasks/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_get_task_not_found(client):

    response = client.get("/tasks/999999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"

# Casos de prueba para la creación de tareas
def test_create_task(client):

    response = client.post(
        "/tasks", 
        json={
            "title": "Tarea creada desde Pytest",
            "completed": False
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Tarea creada desde Pytest"
    assert data["completed"] == False
    assert "id" in data
    
    
def test_create_task_without_title(client):

    response = client.post(
        "/tasks", 
        json={
            "completed": False
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'title' es obligatorio"


def test_create_task_with_empty_title(client):

    response = client.post(
        "/tasks", 
        json={
            "title": "",
            "completed": False
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El campo 'title' es obligatorio"


def test_create_task_with_invalid_completed(client):

    response = client.post(
        "/tasks", 
        json={
            "title": "Tarea invalida",
            "completed": "false"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'completed' debe ser un booleano"


# Casos de prueba para la actualización de tareas
def test_update_task_title(client):

    response = client.patch(
        "/tasks/1",
        json={
            "title": "Título actualizado"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["title"] == "Título actualizado"


def test_update_task_completed(client):

    response = client.patch(
        "/tasks/1",
        json={
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["completed"] is True


def test_update_task_with_empty_title(client):

    response = client.patch(
        "/tasks/1",
        json={
            "title": ""
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'title' debe ser un texto no vacío"


def test_update_task_with_invalid_completed(client):

    response = client.patch(
        "/tasks/1",
        json={
            "completed": "true"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "'completed' debe ser un booleano"
    

def test_update_task_not_found(client):

    response = client.patch(
        "/tasks/999999",
        json={
            "title": "Tarea inexistente"
        }
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"


# Casos de prueba para la eliminación de tareas
def test_delete_task(client):

    response = client.delete("/tasks/1")

    assert response.status_code == 204


def test_delete_task_not_found(client):

    response = client.delete("/tasks/999999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Tarea no encontrada"


# Casos de prueba para la creación de tareas con cuerpo inválido
def test_create_task_with_invalid_body(client):
    response = client.post(
        "/tasks",
        json=[]
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"
    

def test_update_task_with_invalid_body(client):
    response = client.patch(
        "/tasks/1",
        json=[]
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "El cuerpo debe ser un objeto JSON"
    

# Casos de prueba para rutas no encontradas
def test_route_not_found(client):
    response = client.get("/ruta-que-no-existe")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Recurso no encontrado"

def test_method_not_allowed(client):
    response = client.post("/tasks/1")

    assert response.status_code == 405

    data = response.get_json()

    assert data["error"] == "Método no permitido"

def test_internal_server_error(client):
    app = client.application

    app.config["PROPAGATE_EXCEPTIONS"] = False

    @app.route("/trigger-500-test")
    def trigger_500_test():
        raise Exception("Error de prueba")

    response = client.get("/trigger-500-test")

    assert response.status_code == 500

    data = response.get_json()

    assert data["error"] == "Error interno del servidor"