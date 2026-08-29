from flask import Blueprint, jsonify, request
from models import db, User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "El campo 'username' es obligatorio"}), 400

    if not isinstance(password, str) or not password:
        return jsonify({"error": "El campo 'password' es obligatorio"}), 400

    username = username.strip()

    existing_user = User.query.filter_by(username=username).first()

    if existing_user is not None:
        return jsonify({"error": "El usuario ya existe"}), 409

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "El campo 'username' es obligatorio"}), 400

    if not isinstance(password, str) or not password:
        return jsonify({"error": "El campo 'password' es obligatorio"}), 400

    user = User.query.filter_by(username=username.strip()).first()

    if user is None or not user.check_password(password):
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token
    }), 200