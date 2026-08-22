from flask import Blueprint, jsonify, request
from models import db, Task

tasks_bp = Blueprint("tasks", __name__)

# Ruta para obtener todas las tareas
# GET /tasks obtiene todas las tareas de la base de datos y las devuelve en formato JSON.
@tasks_bp.get("/tasks")
def get_tasks():
    tasks_from_db = Task.query.all()

    return jsonify([task.to_dict() for task in tasks_from_db])


# GET /tasks/<int:task_id> obtiene una tarea específica por su ID
@tasks_bp.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    return jsonify(task.to_dict())


# POST /tasks crea una nueva tarea en la base de datos
@tasks_bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}

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
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json(silent=True) or {}

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
def delete_task(task_id):
    task = db.session.get(Task, task_id)

    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    db.session.delete(task)
    db.session.commit()

    return "", 204