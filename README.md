# Flask Tasks API

API REST para gestionar tareas desarrollada con **Python, Flask, Flask-SQLAlchemy y SQLite**.

Este proyecto fue creado como práctica de desarrollo backend y tiene como objetivo implementar una API CRUD completa para crear, consultar, modificar y eliminar tareas.

La aplicación utiliza una base de datos SQLite para almacenar las tareas y Flask-SQLAlchemy para interactuar con la base de datos mediante un modelo `Task`.

Además, las rutas están organizadas utilizando **Flask Blueprints**, separando la configuración principal de la aplicación de las rutas relacionadas con las tareas.

---

## 📌 Características

La API permite:

- Crear nuevas tareas.
- Obtener todas las tareas.
- Obtener una tarea específica por su ID.
- Actualizar parcialmente una tarea.
- Eliminar una tarea.
- Validar los datos recibidos.
- Devolver códigos de estado HTTP apropiados.
- Persistir las tareas en una base de datos SQLite.
- Organizar las rutas mediante Flask Blueprints.

---

## 🛠️ Tecnologías utilizadas

### Python

Lenguaje utilizado para desarrollar la aplicación backend.

### Flask

Framework utilizado para crear la API REST y definir los diferentes endpoints.

### Flask-SQLAlchemy

Extensión de Flask que permite trabajar con SQLAlchemy y utilizar una base de datos relacional mediante modelos Python.

### SQLAlchemy

ORM utilizado para interactuar con la base de datos sin tener que escribir directamente las consultas SQL más comunes.

### SQLite

Base de datos utilizada para almacenar las tareas.

### Postman

Utilizado para probar los diferentes endpoints de la API.

### Git y GitHub

Utilizados para controlar las versiones del proyecto y almacenar el código fuente.

---

# 📁 Estructura del proyecto

```text
flask-tasks-api/
│
├── app.py
├── models.py
├── requirements.txt
├── README.md
│
├── routes/
│   ├── __init__.py
│   └── tasks.py
│
└── postman/

---

### app.py

Es el punto de entrada de la aplicación.

Se encarga de:

- Crear la aplicación Flask.
- Configurar la conexión con SQLite.
- Inicializar SQLAlchemy.
- Crear las tablas de la base de datos.
- Registrar el Blueprint de tareas.
- Iniciar el servidor.

---

### models.py

Contiene la configuración de SQLAlchemy y el modelo `Task`.

El modelo representa una tarea dentro de la base de datos.

Cada tarea tiene los siguientes campos:

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | Integer | Identificador único de la tarea |
| `title` | String | Título de la tarea |
| `completed` | Boolean | Indica si la tarea está completada |

---

### routes/tasks.py

Contiene todos los endpoints relacionados con las tareas.

Las rutas están organizadas utilizando un Blueprint llamado `tasks_bp`. Esto permite mantener separada la configuración principal de Flask de las rutas de la API.

---

### requirements.txt

Contiene las dependencias necesarias para ejecutar el proyecto.

---

### postman/

Contiene los recursos utilizados para realizar las pruebas de la API mediante Postman.

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone [https://github.com/ValentinMesa06/flask-tasks-api.git](https://github.com/ValentinMesa06/flask-tasks-api.git)

Entrar en la carpeta del proyecto:

cd flask-tasks-api

### 2. Instalar las dependencias

Ejecutar:

pip install -r requirements.txt

Esto instalará Flask, Flask-SQLAlchemy, SQLAlchemy y las demás dependencias necesarias.

---

# ▶️ Ejecutar la aplicación

Para iniciar el servidor:

python app.py

La API estará disponible en:

http://127.0.0.1:5000

Para detener el servidor:

Ctrl + C

---

# 🔌 Endpoints

La API implementa un CRUD completo para gestionar tareas.

### Método	Endpoint	Descripción
- GET	/tasks	Obtener todas las tareas
- GET	/tasks/<id>	Obtener una tarea específica
- POST	/tasks	Crear una nueva tarea
- PATCH	/tasks/<id>	Actualizar una tarea
- DELETE	/tasks/<id>	Eliminar una tarea

---

### 📋 GET /tasks

Obtiene todas las tareas almacenadas en la base de datos.

Request
GET http://127.0.0.1:5000/tasks
Response
[
    {
        "id": 1,
        "title": "Aprender Flask",
        "completed": false
    },
    {
        "id": 2,
        "title": "Aprender SQLAlchemy",
        "completed": true
    }
]

El endpoint devuelve una lista con todas las tareas almacenadas.

---

### 🔎 GET /tasks/<id>

Obtiene una tarea específica utilizando su ID.

Request
GET http://127.0.0.1:5000/tasks/1
Response
{
    "id": 1,
    "title": "Aprender Flask",
    "completed": false
}
Tarea inexistente

Si el ID no corresponde a ninguna tarea:

GET http://127.0.0.1:5000/tasks/999

La API devuelve:

{
    "error": "Tarea no encontrada"
}

con código HTTP:

404 Not Found

---

### ➕ POST /tasks

Crea una nueva tarea.

Request
POST http://127.0.0.1:5000/tasks

El cuerpo de la petición debe enviarse en formato JSON.

Body
{
    "title": "Aprender Flask",
    "completed": false
}

El campo completed es opcional. Si no se proporciona, su valor será false.

Response

Si la tarea se crea correctamente:

{
    "id": 3,
    "title": "Aprender Flask",
    "completed": false
}

La API devuelve:

201 Created
Validaciones

El campo title es obligatorio y debe contener un texto no vacío.

Ejemplo inválido:

{
    "title": ""
}

Respuesta:

{
    "error": "El campo 'title' es obligatorio"
}

La API devuelve:

400 Bad Request

También se valida que completed sea un booleano.

Ejemplo válido:

{
    "title": "Estudiar Python",
    "completed": true
}

Ejemplo inválido:

{
    "title": "Estudiar Python",
    "completed": "true"
}

En este caso la API devuelve un error 400 Bad Request.

---

### ✏️ PATCH /tasks/<id>

Permite modificar parcialmente una tarea existente.

A diferencia de POST, no es necesario enviar todos los campos de la tarea.

Request
PATCH http://127.0.0.1:5000/tasks/1

Por ejemplo, para marcar una tarea como completada:

{
    "completed": true
}
Response
{
    "id": 1,
    "title": "Aprender Flask",
    "completed": true
}

También es posible modificar solamente el título:

{
    "title": "Aprender Flask y SQLAlchemy"
}
Validaciones

Si se proporciona title, debe ser un texto no vacío.

Ejemplo inválido:

{
    "title": ""
}

También se valida que completed sea un booleano.

Ejemplo inválido:

{
    "completed": "true"
}

Si la tarea no existe:

PATCH http://127.0.0.1:5000/tasks/999

La API devuelve:

{
    "error": "Tarea no encontrada"
}

con código:

404 Not Found

---

### 🗑️ DELETE /tasks/<id>

Elimina una tarea de la base de datos.

Request
DELETE http://127.0.0.1:5000/tasks/1

Si la eliminación es exitosa, la API devuelve:

204 No Content

El código 204 indica que la operación se realizó correctamente y que no hay contenido adicional que devolver.

Tarea inexistente

Si se intenta eliminar una tarea que no existe:

DELETE http://127.0.0.1:5000/tasks/999

La API devuelve:

{
    "error": "Tarea no encontrada"
}

con código:

404 Not Found

---

# 🚦 Códigos de estado HTTP

La API utiliza diferentes códigos HTTP dependiendo del resultado de cada operación.

Código	Significado	Uso
- 200	OK	Peticiones exitosas
- 201	Created	Tarea creada correctamente
- 204	No Content	Tarea eliminada correctamente
- 400	Bad Request	Datos enviados incorrectamente
- 404	Not Found	Tarea inexistente

---

# 🗄️ Base de datos

El proyecto utiliza SQLite como sistema de base de datos.

La conexión se realiza utilizando Flask-SQLAlchemy.

El modelo principal de la aplicación es Task:

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

Cada objeto Task representa una fila dentro de la tabla de tareas.

La base de datos se crea automáticamente al iniciar la aplicación.

---

## 🧩 Flask Blueprint

Las rutas de la API están organizadas utilizando un Blueprint:

tasks_bp = Blueprint("tasks", __name__)

Las rutas relacionadas con las tareas se encuentran en:

routes/tasks.py

Posteriormente, el Blueprint se registra en app.py:

app.register_blueprint(tasks_bp)

Esta organización permite separar las rutas de la configuración principal de Flask y facilita que el proyecto pueda crecer en el futuro.

---

### 🔄 Funcionamiento de la API

El flujo general de una petición es:

Cliente
   │
   │ HTTP Request
   ▼
Flask
   │
   ▼
Blueprint (tasks.py)
   │
   ▼
Modelo Task
   │
   ▼
SQLAlchemy
   │
   ▼
SQLite
   │
   │
   ▼
Respuesta JSON
   │
   ▼
Cliente

Por ejemplo, cuando un cliente realiza:

POST /tasks

la petición llega a Flask y es dirigida al endpoint correspondiente dentro del Blueprint.

Luego se validan los datos recibidos, se crea un objeto Task, SQLAlchemy guarda la información en SQLite y finalmente la API devuelve la tarea creada en formato JSON.

---

# 🧪 Pruebas con Postman

Los endpoints fueron probados utilizando Postman.

Las operaciones principales probadas son:

GET     /tasks
GET     /tasks/<id>
POST    /tasks
PATCH   /tasks/<id>
DELETE  /tasks/<id>

También se probaron diferentes casos de error, incluyendo:

Crear una tarea sin title.
Crear una tarea con title vacío.
Crear una tarea con completed incorrecto.
Actualizar una tarea con datos inválidos.
Consultar una tarea inexistente.
Modificar una tarea inexistente.
Eliminar una tarea inexistente.
📚 Conceptos aplicados

Durante el desarrollo del proyecto se aplicaron diferentes conceptos de desarrollo backend:

- APIs REST.
- Métodos HTTP.
- CRUD.
- JSON.
- Códigos de estado HTTP.
- Validación de datos.
- Flask.
- Flask Blueprints.
- ORM.
- SQLAlchemy.
- Bases de datos relacionales.
- SQLite.
- Separación de responsabilidades.
- Persistencia de datos.
- Control de versiones con Git.

---

# 🚀 Próximas mejoras

Algunas funcionalidades que pueden incorporarse en futuras versiones:

 - Implementar tests automatizados con Pytest.
 - Mejorar el manejo global de errores.
 - Separar la lógica de negocio en una capa de servicios.
 - Agregar documentación con Swagger / OpenAPI.
 - Utilizar variables de entorno.
 - Agregar paginación.
 - Agregar filtros por estado de las tareas.
 - Implementar búsqueda de tareas.
 - Dockerizar la aplicación.
 - Realizar el deploy de la API.

---

# 👨‍💻 Autor

Valentín Mesa

GitHub:

https://github.com/ValentinMesa06
