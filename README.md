# Flask Tasks API

API REST para gestionar tareas desarrollada con **Python, Flask y Flask-SQLAlchemy**.

El proyecto implementa un CRUD completo de tareas, persistencia de datos mediante SQLite, validaciones de entrada, arquitectura organizada mediante Blueprints, tests automatizados con Pytest y un workflow de integración continua mediante GitHub Actions.

---

## 📌 Características

- API REST desarrollada con Flask.
- CRUD completo de tareas.
- Persistencia de datos utilizando SQLite.
- ORM mediante Flask-SQLAlchemy.
- Organización de rutas utilizando Flask Blueprints.
- Validación de datos recibidos en las peticiones.
- Manejo de errores HTTP.
- Respuestas en formato JSON.
- Tests automatizados utilizando Pytest.
- 16 tests automatizados.
- 100% de cobertura de código.
- Base de datos independiente para los tests.
- Integración continua mediante GitHub Actions.
- Verificación automática de los tests en cada `push` a `main`.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Flask | Framework web |
| Flask-SQLAlchemy | ORM y conexión con SQLite |
| SQLAlchemy | Gestión de la base de datos |
| SQLite | Base de datos |
| Pytest | Tests automatizados |
| pytest-cov | Medición de cobertura |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| GitHub Actions | Integración continua |

---

## 📂 Estructura del proyecto

```text
flask-tasks-api/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── instance/
│   └── tasks.db
│
├── routes/
│   ├── __init__.py
│   └── tasks.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_tasks.py
│
├── .gitignore
├── app.py
├── models.py
├── requirements.txt
└── README.md
```

### Descripción de los principales archivos

**`app.py`**: archivo principal de la aplicación. Crea la aplicación Flask, configura SQLAlchemy, inicializa la base de datos y registra los Blueprints.

**`models.py`**: contiene los modelos de SQLAlchemy. Actualmente se encuentra definido el modelo `Task`.

**`routes/tasks.py`**: contiene los endpoints relacionados con las tareas.

**`tests/`**: contiene los tests automatizados de la API y las fixtures utilizadas para crear un entorno de pruebas aislado.

**`.github/workflows/tests.yml`**: define el workflow de GitHub Actions encargado de ejecutar automáticamente los tests.

**`requirements.txt`**: contiene las dependencias necesarias para ejecutar el proyecto.

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/ValentinMesa06/flask-tasks-api.git
cd flask-tasks-api
```

## 2. Crear un entorno virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecutar la aplicación

```bash
python app.py
```

La API estará disponible normalmente en `http://127.0.0.1:5000` o `http://localhost:5000`.

---

# 📋 Modelo `Task`

```json
{
	"id": 1,
	"title": "Aprender Flask",
	"completed": false
}
```

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer | Identificador único de la tarea |
| `title` | String | Título de la tarea |
| `completed` | Boolean | Indica si la tarea está completada |

El campo `id` es generado automáticamente por la base de datos. `completed` tiene `false` como valor predeterminado.

---

# 🔌 Endpoints

## Obtener todas las tareas

```http
GET /tasks
```

```bash
curl http://127.0.0.1:5000/tasks
```

Devuelve una lista de tareas con código `200 OK`.

## Obtener una tarea

```http
GET /tasks/<id>
```

```bash
curl http://127.0.0.1:5000/tasks/1
```

Devuelve la tarea con código `200 OK`. Si no existe:

```json
{"error": "Tarea no encontrada"}
```

Código `404 Not Found`.

## Crear una tarea

```http
POST /tasks
Content-Type: application/json
```

```json
{
	"title": "Aprender Flask",
	"completed": false
}
```

El campo `completed` es opcional y utiliza `false` por defecto. Devuelve la tarea creada con código `201 Created`.

## Actualizar una tarea

```http
PATCH /tasks/<id>
```

Permite modificar uno o varios campos (`title` y `completed`) de una tarea existente. Devuelve la tarea actualizada con código `200 OK`.

## Eliminar una tarea

```http
DELETE /tasks/<id>
```

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

Si la tarea existe, se elimina de la base de datos y devuelve `204 No Content`.

---

# ⚠️ Validaciones

- `title` es obligatorio y debe ser un texto no vacío.
- `completed` debe ser un booleano.
- Las peticiones que crean o modifican tareas deben recibir un objeto JSON.

Ejemplos de errores:

```json
{"error": "El campo 'title' es obligatorio"}
```

```json
{"error": "'completed' debe ser un booleano"}
```

```json
{"error": "El cuerpo debe ser un objeto JSON"}
```

Todos corresponden a `400 Bad Request`.

---

# 🧪 Tests

El proyecto utiliza **Pytest** y cuenta actualmente con 16 tests, 100% de cobertura y 0 warnings.

```bash
pytest
pytest --cov=. --cov-report=term-missing
```

Los tests utilizan una base de datos independiente para evitar modificar los datos reales.

---

# 🔄 Integración continua

El workflow `.github/workflows/tests.yml` ejecuta automáticamente los tests en cada `push` a `main` y en Pull Requests hacia `main`.

Proceso: configurar Python → instalar dependencias → ejecutar Pytest → verificar los 16 tests y el 100% de cobertura.

---

# 🗄️ Base de datos

La aplicación utiliza SQLite mediante Flask-SQLAlchemy. La base de datos de desarrollo se encuentra en `instance/tasks.db` y contiene la tabla `Task` con los campos `id`, `title` y `completed`.

---

# 📮 Probar la API con Postman

La API puede probarse utilizando [Postman](https://www.postman.com/).

URL base: `http://127.0.0.1:5000`

```text
GET     /tasks
GET     /tasks/1
POST    /tasks
PATCH   /tasks/1
DELETE  /tasks/1
```

Para `POST` y `PATCH`, seleccionar **Body → raw → JSON**.

---

# 📈 Estado del proyecto

El proyecto cuenta con configuración inicial de Flask, API REST, CRUD de tareas, SQLite, Flask-SQLAlchemy, modelo `Task`, Blueprints, validaciones, manejo de errores, tests con Pytest, fixtures, base de datos aislada, 16 tests automatizados, 100% de cobertura, GitHub Actions e integración continua.

---

# 🚧 Próximas mejoras

- Documentación Swagger / OpenAPI
- Variables de entorno para la configuración
- Manejo global de errores
- Paginación, filtros y ordenamiento de tareas
- Autenticación de usuarios
- Tests de integración adicionales
- Dockerización y deploy de la API
- Base de datos PostgreSQL para producción

---

# 👨‍💻 Autor

**Valentín Mesa**

Proyecto desarrollado como práctica para aprender y aplicar conceptos de desarrollo de APIs REST utilizando Python y Flask.

---

# 📄 Licencia

Este proyecto se encuentra disponible para fines educativos y de aprendizaje.
