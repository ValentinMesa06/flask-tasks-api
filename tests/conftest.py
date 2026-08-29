import tempfile
import pytest

from app import create_app
from models import db, User, Task


@pytest.fixture
def client():
    _, db_path = tempfile.mkstemp(suffix=".db")

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
        "JWT_SECRET_KEY": "clave-secreta-para-tests-32-bytes-minimo"
    })

    with app.app_context():
        db.create_all()

        user = User(
            username="usuario_test"
        )

        user.set_password("password123")

        db.session.add(user)
        db.session.commit()

        task = Task(
            title="Tarea de prueba",
            completed=False,
            user_id=user.id
        )

        db.session.add(task)
        db.session.commit()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.engine.dispose()


@pytest.fixture
def auth_headers(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "usuario_test",
            "password": "password123"
        }
    )

    token = response.get_json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }