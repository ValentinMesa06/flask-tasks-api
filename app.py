import os

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from models import db
from routes.tasks import tasks_bp
from routes.auth import auth_bp


def create_app(test_config=None):
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ.get( "JWT_SECRET_KEY", "clave-secreta-para-desarrollo" )

    # Si estamos ejecutando tests, usamos la configuración de los tests
    if test_config:
        app.config.update(test_config)

    # Inicializar extensiones
    db.init_app(app)
    JWTManager(app)

    # Registrar rutas
    app.register_blueprint(tasks_bp)
    app.register_blueprint(auth_bp)

    # Manejo de errores
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Recurso no encontrado"}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Método no permitido"}), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Error interno del servidor"}), 500

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)