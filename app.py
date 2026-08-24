from flask import Flask
from models import db
from flasgger import Swagger
from routes.tasks import tasks_bp


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(tasks_bp)
    
    swagger = Swagger(app)

    return app


app = create_app()


if __name__ == "__main__": # pragma: no cover
    app.run(debug=True) # pragma: no cover