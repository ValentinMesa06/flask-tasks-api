# Flask Tasks API

API REST para gestionar tareas, desarrollada con **Python y Flask**. El proyecto implementa autenticación de usuarios mediante **JWT**, persistencia de datos con **SQLite y SQLAlchemy**, validación de solicitudes y tests automatizados con **pytest**.

## 🚀 Características

* Registro de usuarios.
* Inicio de sesión mediante JWT.
* Contraseñas almacenadas de forma segura mediante hashing.
* Creación de tareas.
* Consulta de tareas.
* Consulta de una tarea por ID.
* Actualización parcial de tareas.
* Eliminación de tareas.
* Cada usuario puede acceder únicamente a sus propias tareas.
* Validación de datos recibidos.
* Manejo de errores HTTP.
* Tests automatizados con pytest.
* 100% de cobertura de código en los tests actuales.

## 🛠️ Tecnologías utilizadas

* **Python 3**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLAlchemy**
* **Flask-JWT-Extended**
* **SQLite**
* **Pytest**
* **Pytest-Cov**
* **Postman**

## 📁 Estructura del proyecto

```text
flask-tasks-api/
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── tasks.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_config.py
│   ├── test_models.py
│   └── test_tasks.py
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ValentinMesa06/flask-tasks-api.git
```

### 2. Entrar en el proyecto

```bash
cd flask-tasks-api
```

### 3. Crear un entorno virtual

Windows:

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación

Ejecutar:

```bash
python app.py
```

La API estará disponible en:

```text
http://127.0.0.1:5000
```

---

# 🔐 Autenticación

La API utiliza **JSON Web Tokens (JWT)** para proteger los endpoints relacionados con las tareas.

## Registrar un usuario

**POST**

```text
/auth/register
```

Body:

```json
{
    "username": "usuario1",
    "password": "password123"
}
```

Respuesta:

```json
{
    "id": 1,
    "username": "usuario1"
}
```

## Iniciar sesión

**POST**

```text
/auth/login
```

Body:

```json
{
    "username": "usuario1",
    "password": "password123"
}
```

Respuesta:

```json
{
    "access_token": "JWT_TOKEN"
}
```

El token obtenido debe enviarse en las solicitudes protegidas utilizando:

```text
Authorization: Bearer JWT_TOKEN
```

---

# 📋 Endpoints

## 🔑 Autenticación

| Método | Endpoint         | Descripción                  | Autenticación |
| ------ | ---------------- | ---------------------------- | ------------- |
| POST   | `/auth/register` | Registrar un usuario         | No            |
| POST   | `/auth/login`    | Iniciar sesión y obtener JWT | No            |

## 📝 Tareas

| Método | Endpoint      | Descripción                    | Autenticación |
| ------ | ------------- | ------------------------------ | ------------- |
| GET    | `/tasks`      | Obtener las tareas del usuario | Sí            |
| GET    | `/tasks/<id>` | Obtener una tarea específica   | Sí            |
| POST   | `/tasks`      | Crear una nueva tarea          | Sí            |
| PATCH  | `/tasks/<id>` | Actualizar una tarea           | Sí            |
| DELETE | `/tasks/<id>` | Eliminar una tarea             | Sí            |

---

# 📝 Ejemplos de uso

## Obtener tareas

**GET**

```text
/tasks
```

Header:

```text
Authorization: Bearer JWT_TOKEN
```

Respuesta:

```json
[
    {
        "id": 1,
        "title": "Aprender Flask",
        "completed": false
    }
]
```

## Crear una tarea

**POST**

```text
/tasks
```

Body:

```json
{
    "title": "Aprender Flask y JWT",
    "completed": false
}
```

Respuesta:

```json
{
    "id": 2,
    "title": "Aprender Flask y JWT",
    "completed": false
}
```

## Actualizar una tarea

**PATCH**

```text
/tasks/1
```

Body:

```json
{
    "completed": true
}
```

Respuesta:

```json
{
    "id": 1,
    "title": "Aprender Flask",
    "completed": true
}
```

## Eliminar una tarea

**DELETE**

```text
/tasks/1
```

Respuesta:

```text
204 No Content
```

---

# ❌ Manejo de errores

La API devuelve respuestas JSON para diferentes errores HTTP.

### 400 — Solicitud inválida

Ejemplo:

```json
{
    "error": "El campo 'title' es obligatorio"
}
```

### 401 — No autorizado

Ejemplo:

```json
{
    "error": "Usuario o contraseña incorrectos"
}
```

### 404 — Recurso no encontrado

Ejemplo:

```json
{
    "error": "Tarea no encontrada"
}
```

### 405 — Método no permitido

Ejemplo:

```json
{
    "error": "Método no permitido"
}
```

### 500 — Error interno

Ejemplo:

```json
{
    "error": "Error interno del servidor"
}
```

---

# 🧪 Tests

El proyecto utiliza **pytest** para realizar pruebas automatizadas.

Para ejecutar todos los tests:

```bash
pytest
```

Para ejecutar los tests mostrando cobertura:

```bash
pytest --cov=.
```

Estado actual:

```text
40 passed
99% coverage
```

Los tests cubren:

* Registro de usuarios.
* Login.
* Validaciones de autenticación.
* Modelo de usuarios.
* Modelo de tareas.
* Obtención de tareas.
* Creación de tareas.
* Actualización de tareas.
* Eliminación de tareas.
* Validación de datos.
* Rutas inexistentes.
* Métodos HTTP no permitidos.
* Errores internos.
* Autorización mediante JWT.
* Aislamiento de tareas entre usuarios.

---

# 🔒 Seguridad

El proyecto implementa varias medidas básicas de seguridad:

* Las contraseñas no se almacenan en texto plano.
* Se utiliza hashing mediante Werkzeug.
* Los endpoints de tareas requieren autenticación JWT.
* Cada tarea está asociada a un usuario.
* Los usuarios solamente pueden acceder a sus propias tareas.
* El `user_id` no es enviado por el cliente al crear una tarea; se obtiene a partir del usuario autenticado.

---

# 📌 Estado del proyecto

Proyecto funcional y en desarrollo.

Actualmente cuenta con:

* ✅ API REST funcional.
* ✅ CRUD de tareas.
* ✅ Autenticación JWT.
* ✅ Autorización por usuario.
* ✅ SQLite + SQLAlchemy.
* ✅ Validaciones.
* ✅ Manejo de errores.
* ✅ Tests automatizados.
* ✅ 100% de cobertura en los tests actuales.
* ✅ Pruebas manuales realizadas con Postman.

---

# 👨‍💻 Autor

**Valentín Santiago Mesa**

GitHub:
https://github.com/ValentinMesa06

