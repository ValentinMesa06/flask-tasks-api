import tempfile

import pytest

from app import create_app
from models import db, Task


@pytest.fixture
def client():
    _, db_path = tempfile.mkstemp(suffix=".db")

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}"
    })

    with app.app_context():
        db.create_all()

        task = Task(
            title="Tarea de prueba",
            completed=False
        )

        db.session.add(task)
        db.session.commit()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.engine.dispose()