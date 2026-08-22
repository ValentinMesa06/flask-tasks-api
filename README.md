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
