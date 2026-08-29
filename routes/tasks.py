from flask import Blueprint, jsonify, request
from models import db, Task
from flask_jwt_extended import jwt_required, get_jwt_identity


tasks_bp = Blueprint("tasks", __name__)


# ============================================================
# GET /tasks
# Obtener todas las tareas del usuario autenticado
# ============================================================

@tasks_bp.get("/tasks")
@jwt_required()
def get_tasks():
    """
    Obtener todas las tareas
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Lista de tareas del usuario autenticado
    """

    user_id = int(get_jwt_identity())

    tasks_from_db = Task.query.filter_by(
        user_id=user_id
    ).all()

    return jsonify([
        task.to_dict()
        for task in tasks_from_db
    ])


# ============================================================
# GET /tasks/<task_id>
# Obtener una tarea específica
# ============================================================

@tasks_bp.get("/tasks/<int:task_id>")
@jwt_required()
def get_task(task_id):
    """
    Obtener una tarea por ID
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Tarea encontrada
      404:
        description: Tarea no encontrada
    """

    user_id = int(get_jwt_identity())

    task = Task.query.filter_by(
        id=task_id,
        user_id=user_id
    ).first()

    if task is None:
        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    return jsonify(task.to_dict())


# ============================================================
# POST /tasks
# Crear una nueva tarea
# ============================================================

@tasks_bp.post("/tasks")
@jwt_required()
def create_task():
    """
    Crear una nueva tarea
    ---
    tags:
      - Tasks
    """

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "El cuerpo debe ser un objeto JSON"
        }), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "El campo 'title' es obligatorio"
        }), 400

    completed = data.get("completed", False)

    if not isinstance(completed, bool):
        return jsonify({
            "error": "'completed' debe ser un booleano"
        }), 400

    user_id = int(get_jwt_identity())

    task = Task(
        title=title.strip(),
        completed=completed,
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


# ============================================================
# PATCH /tasks/<task_id>
# Actualizar una tarea
# ============================================================

@tasks_bp.patch("/tasks/<int:task_id>")
@jwt_required()
def update_task(task_id):
    """
    Actualizar una tarea
    ---
    tags:
      - Tasks
    """

    user_id = int(get_jwt_identity())

    task = Task.query.filter_by(
        id=task_id,
        user_id=user_id
    ).first()

    if task is None:
        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "El cuerpo debe ser un objeto JSON"
        }), 400

    if "title" in data:

        if (
            not isinstance(data["title"], str)
            or not data["title"].strip()
        ):
            return jsonify({
                "error": "'title' debe ser un texto no vacío"
            }), 400

        task.title = data["title"].strip()

    if "completed" in data:

        if not isinstance(data["completed"], bool):
            return jsonify({
                "error": "'completed' debe ser un booleano"
            }), 400

        task.completed = data["completed"]

    db.session.commit()

    return jsonify(task.to_dict())


# ============================================================
# DELETE /tasks/<task_id>
# Eliminar una tarea
# ============================================================

@tasks_bp.delete("/tasks/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    """
    Eliminar una tarea
    ---
    tags:
      - Tasks
    """

    user_id = int(get_jwt_identity())

    task = Task.query.filter_by(
        id=task_id,
        user_id=user_id
    ).first()

    if task is None:
        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return "", 204