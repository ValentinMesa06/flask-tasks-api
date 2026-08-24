from flask import Blueprint, jsonify, request
from models import db, Task

tasks_bp = Blueprint("tasks", __name__)

# Ruta para obtener todas las tareas
# GET /tasks obtiene todas las tareas de la base de datos y las devuelve en formato JSON.
@tasks_bp.get("/tasks")
def get_tasks():
    """
    Obtener todas las tareas
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Lista de todas las tareas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              title:
                type: string
                example: "Aprender Flask"
              completed:
                type: boolean
                example: false
    """
    
    tasks_from_db = Task.query.all()

    return jsonify([task.to_dict() for task in tasks_from_db])


# GET /tasks/<int:task_id> obtiene una tarea específica por su ID
@tasks_bp.get("/tasks/<int:task_id>")
def get_task(task_id):
    """
    Obtener una tarea por ID
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID de la tarea
        example: 1
    responses:
      200:
        description: Tarea encontrada
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: "Aprender Flask"
            completed:
              type: boolean
              example: false
      404:
        description: Tarea no encontrada
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Tarea no encontrada"
    """
    
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    return jsonify(task.to_dict())


# POST /tasks crea una nueva tarea en la base de datos
@tasks_bp.post("/tasks")
def create_task():
    """
    Crear una nueva tarea
    ---
    tags:
      - Tasks
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
          properties:
            title:
              type: string
              example: "Aprender Flask"
            completed:
              type: boolean
              example: false
    responses:
      201:
        description: Tarea creada correctamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: "Aprender Flask"
            completed:
              type: boolean
              example: false
      400:
        description: Datos inválidos
        schema:
          type: object
          properties:
            error:
              type: string
              example: "El campo 'title' es obligatorio"
    """
    
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "El campo 'title' es obligatorio"}), 400

    completed = data.get("completed", False)

    if not isinstance(completed, bool):
        return jsonify({"error": "'completed' debe ser un booleano"}), 400

    task = Task(
        title=title.strip(),
        completed=completed
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


# PATCH /tasks/<int:task_id> actualiza una tarea existente
@tasks_bp.patch("/tasks/<int:task_id>")
def update_task(task_id):
    """
    Actualizar una tarea
    ---
    tags:
      - Tasks
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID de la tarea
        example: 1
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Aprender Flask y SQLAlchemy"
            completed:
              type: boolean
              example: true
    responses:
      200:
        description: Tarea actualizada correctamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: "Aprender Flask y SQLAlchemy"
            completed:
              type: boolean
              example: true
      400:
        description: Datos inválidos
        schema:
          type: object
          properties:
            error:
              type: string
              example: "'title' debe ser un texto no vacío"
      404:
        description: Tarea no encontrada
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Tarea no encontrada"
    """
    
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return jsonify({"error": "'title' debe ser un texto no vacío"}), 400

        task.title = data["title"].strip()

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({"error": "'completed' debe ser un booleano"}), 400

        task.completed = data["completed"]

    db.session.commit()

    return jsonify(task.to_dict())


# DELETE /tasks/<int:task_id> elimina una tarea existente
@tasks_bp.delete("/tasks/<int:task_id>")
@tasks_bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    """
    Eliminar una tarea
    ---
    tags:
      - Tasks
    produces:
      - application/json
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID de la tarea que se desea eliminar
        example: 1
    responses:
      204:
        description: Tarea eliminada correctamente
      404:
        description: Tarea no encontrada
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Tarea no encontrada"
    """
    
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    db.session.delete(task)
    db.session.commit()

    return "", 204