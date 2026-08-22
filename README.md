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

app.py

Es el punto de entrada de la aplicación.

Se encarga de:

    Crear la aplicación Flask.

    Configurar la base de datos.

    Inicializar SQLAlchemy.

    Crear las tablas de la base de datos.

    Registrar el Blueprint de tareas.

    Iniciar el servidor.

models.py

Contiene la configuración de SQLAlchemy y el modelo Task.

El modelo representa una tarea dentro de la base de datos.

Cada tarea tiene los siguientes campos:
Campo	Tipo	Descripción
id	Integer	Identificador único de la tarea
title	String	Título de la tarea
completed	Boolean	Indica si la tarea está completada
routes/tasks.py

Contiene todos los endpoints relacionados con las tareas.

Las rutas están organizadas utilizando un Blueprint llamado tasks_bp.

Esto permite mantener separada la lógica de las rutas de la configuración principal de Flask.
requirements.txt

Contiene las dependencias necesarias para ejecutar el proyecto.
⚙️ Instalación
1. Clonar el repositorio

git clone https://github.com/ValentinMesa06/flask-tasks-api.git

Entrar en la carpeta:

cd flask-tasks-api

2. Instalar las dependencias

Ejecutar:

pip install -r requirements.txt

Esto instalará Flask, Flask-SQLAlchemy, SQLAlchemy y las demás dependencias necesarias.
▶️ Ejecutar la aplicación

Para iniciar el servidor:

python app.py

La API estará disponible en:

http://127.0.0.1:5000

🔌 Endpoints

La API implementa un CRUD completo.
Método	Endpoint	Descripción
GET	/tasks	Obtener todas las tareas
GET	/tasks/<id>	Obtener una tarea específica
POST	/tasks	Crear una nueva tarea
PATCH	/tasks/<id>	Actualizar una tarea
DELETE	/tasks/<id>	Eliminar una tarea
📋 GET /tasks

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
🔎 GET /tasks/<id>

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

GET /tasks/999

La API devuelve:

{
    "error": "Tarea no encontrada"
}

con código HTTP:

404 Not Found

➕ POST /tasks

Crea una nueva tarea.
Request

POST http://127.0.0.1:5000/tasks

El cuerpo de la petición debe ser JSON.
Body

{
    "title": "Aprender Flask",
    "completed": false
}

El campo completed es opcional. Si no se proporciona, su valor será:

false

Response

Si la tarea se crea correctamente:

{
    "id": 3,
    "title": "Aprender Flask",
    "completed": false
}

La API devuelve:

201 Created

Validaciones del POST

El campo title es obligatorio.

Por ejemplo:

{
    "title": ""
}

devuelve:

{
    "error": "El campo 'title' es obligatorio"
}

con:

400 Bad Request

También se valida que completed sea un booleano.

Esto es válido:

{
    "title": "Estudiar Python",
    "completed": true
}

Mientras que esto no:

{
    "title": "Estudiar Python",
    "completed": "true"
}

En ese caso la API devuelve un error 400.
✏️ PATCH /tasks/<id>

Permite modificar parcialmente una tarea existente.

A diferencia de POST, no es necesario enviar todos los campos.
Request

PATCH http://127.0.0.1:5000/tasks/1

Por ejemplo, para marcar una tarea como completada:

{
    "completed": true
}

La respuesta será:

{
    "id": 1,
    "title": "Aprender Flask",
    "completed": true
}

También es posible modificar solamente el título:

{
    "title": "Aprender Flask y SQLAlchemy"
}

Validaciones del PATCH

El campo title, si se proporciona, debe ser un texto no vacío.

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

PATCH /tasks/999

se devuelve:

{
    "error": "Tarea no encontrada"
}

con código:

404 Not Found

🗑️ DELETE /tasks/<id>

Elimina una tarea de la base de datos.
Request

DELETE http://127.0.0.1:5000/tasks/1

Si la eliminación es exitosa, la API devuelve:

204 No Content

El código 204 indica que la operación se realizó correctamente pero no hay contenido que devolver.
Tarea inexistente

Si se intenta eliminar una tarea que no existe:

DELETE /tasks/999

la API devuelve:

{
    "error": "Tarea no encontrada"
}

con código:

404 Not Found

🚦 Códigos de estado HTTP

La API utiliza diferentes códigos HTTP dependiendo del resultado de cada operación.
Código	Significado	Uso
200	OK	Peticiones exitosas
201	Created	Tarea creada correctamente
204	No Content	Tarea eliminada correctamente
400	Bad Request	Datos enviados incorrectamente
404	Not Found	Tarea inexistente
🗄️ Base de datos

La aplicación utiliza SQLite como sistema de base de datos.

La configuración se realiza mediante Flask-SQLAlchemy.

El modelo principal es:

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

Cada objeto Task representa una fila dentro de la tabla de tareas.

La base de datos se crea automáticamente cuando se inicia la aplicación.
🧩 Flask Blueprint

Las rutas están organizadas utilizando un Blueprint:

tasks_bp = Blueprint("tasks", __name__)

Las rutas se encuentran en:

routes/tasks.py

y posteriormente se registran en app.py:

app.register_blueprint(tasks_bp)

Esta organización permite separar las rutas de la configuración principal de la aplicación y facilita el crecimiento del proyecto.
🧪 Pruebas con Postman

Los endpoints fueron probados utilizando Postman.

Las operaciones principales probadas son:

GET     /tasks
GET     /tasks/<id>
POST    /tasks
PATCH   /tasks/<id>
DELETE  /tasks/<id>

También se probaron diferentes casos de error, como:

    Crear una tarea sin title.

    Crear una tarea con completed incorrecto.

    Actualizar una tarea con datos inválidos.

    Consultar una tarea inexistente.

    Modificar una tarea inexistente.

    Eliminar una tarea inexistente.

🔄 Flujo general de la aplicación

El funcionamiento básico de la API es:

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

la petición llega a Flask, el Blueprint procesa la ruta, se validan los datos, se crea un objeto Task, SQLAlchemy lo guarda en SQLite y finalmente la API devuelve la tarea creada en formato JSON.
📈 Próximas mejoras

Algunas funcionalidades que pueden incorporarse al proyecto en futuras versiones:

    Tests automatizados con Pytest.

    Manejo global de errores.

    Separación de la lógica de negocio en una capa de servicios.

    Documentación de la API con Swagger / OpenAPI.

    Variables de entorno.

    Paginación de tareas.

    Filtros por estado (completed).

    Búsqueda de tareas.

    Dockerización de la aplicación.

    Deploy de la API.

👨‍💻 Autor

Valentín Mesa

GitHub:

https://github.com/ValentinMesa06


### Una recomendación importante

**No copies literalmente las líneas que empiezan con `[svg](...)` de tu README anterior.** Esos enlaces no son necesarios.

Y hay algo que me gusta especialmente de este README para tu proyecto: **explica las decisiones que ya tomaste**, como por qué existe `models.py`, qué hace `routes/tasks.py`, cómo funciona el Blueprint y cómo se comunica la API con SQLite.

Eso hace que el repositorio no parezca simplemente *"copié un CRUD de Flask"*, sino que demuestra que entendés **cómo está construido y cómo funciona**.

Después de actualizarlo, hacé:

```bash
git add README.md
git commit -m "docs: improve project documentation"
git push origin main
└── postman/
