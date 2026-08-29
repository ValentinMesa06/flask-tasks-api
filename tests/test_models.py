from models import User

# Casos de prueba para el modelo User
def test_user_set_password():
    user = User(username="testuser")
    
    user.set_password("password123")
    
    assert user.password_hash is not None
    assert user.password_hash != "password123"


def test_user_check_password():
    user = User(username="testuser")

    user.set_password("password123")

    assert user.check_password("password123") is True
    assert user.check_password("password_incorrecta") is False