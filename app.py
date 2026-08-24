import os

from flask import Flask, jsonify
from dotenv import load_dotenv
from flasgger import Swagger
from routes.tasks import tasks_bp
from models import db


load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///tasks.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(tasks_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Recurso no encontrado"}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Método no permitido"}), 405
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Error interno del servidor"}), 500

    swagger = Swagger(app)

    return app


app = create_app()


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True)  # pragma: no cover