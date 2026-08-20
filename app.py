from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Aprender Flask", "completed": False},
]


@app.get("/tasks")
def list_tasks():
    return jsonify(tasks)


@app.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(task)


@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "El campo 'title' es obligatorio"}), 400

    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title.strip(),
        "completed": bool(data.get("completed", False)),
    }
    tasks.append(task)
    return jsonify(task), 201


@app.patch("/tasks/<int:task_id>")
def update_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json(silent=True) or {}
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return jsonify({"error": "'title' debe ser un texto no vacío"}), 400
        task["title"] = data["title"].strip()
    if "completed" in data:
        task["completed"] = bool(data["completed"])
    return jsonify(task)


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    tasks.remove(task)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)