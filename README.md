# Django University

Este es un proyecto de ejemplo para una universidad utilizando Django y Django REST Framework.

## Requisitos

- Python 3.12
- Django 5.1.6
- Django REST Framework 3.15.2

## Instalación

1. Clona el repositorio:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd university
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración:

    ```sh
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

## Endpoints

### Autenticación

- `POST /token/`: Obtener un token JWT.
- `POST /token/refresh/`: Refrescar el token JWT.

### Usuarios

- `GET /users/`: Listar todos los usuarios.
- `POST /users/`: Crear un nuevo usuario.
- `GET /users/{id}/`: Obtener un usuario por ID.
- `PUT /users/{id}/`: Actualizar un usuario por ID.
- `DELETE /users/{id}/`: Eliminar un usuario por ID.

### Estudiantes

- `GET /students/`: Listar todos los estudiantes.
- `POST /students/`: Crear un nuevo estudiante.
- `GET /students/{id}/`: Obtener un estudiante por ID.
- `PUT /students/{id}/`: Actualizar un estudiante por ID.
- `DELETE /students/{id}/`: Eliminar un estudiante por ID.
- `GET /students/{id}/subjects/`: Obtener las inscripciones de un estudiante.
- `GET /students/{id}/approved_subjects/`: Obtener las materias aprobadas de un estudiante y su promedio.

### Profesores

- `GET /teachers/`: Listar todos los profesores.
- `POST /teachers/`: Crear un nuevo profesor.
- `GET /teachers/{id}/`: Obtener un profesor por ID.
- `PUT /teachers/{id}/`: Actualizar un profesor por ID.
- `DELETE /teachers/{id}/`: Eliminar un profesor por ID.
- `GET /teachers/{id}/subjects/`: Obtener las materias de un profesor.
- `GET /teachers/{id}/students/`: Obtener los estudiantes de un profesor.
- `GET /teachers/{id}/subjects/{subject_id}/students/`: Obtener los estudiantes de una materia específica de un profesor.
- `GET /teachers/{id}/subjects/{subject_id}/grades/`: Obtener las calificaciones de una materia específica de un profesor.

### Materias

- `GET /subjects/`: Listar todas las materias.
- `POST /subjects/`: Crear una nueva materia.
- `GET /subjects/{id}/`: Obtener una materia por ID.
- `PUT /subjects/{id}/`: Actualizar una materia por ID.
- `DELETE /subjects/{id}/`: Eliminar una materia por ID.

### Inscripciones

- `GET /inscriptions/`: Listar todas las inscripciones.
- `POST /inscriptions/`: Crear nuevas inscripciones.
- `GET /inscriptions/{id}/`: Obtener una inscripción por ID.
- `PUT /inscriptions/{id}/`: Actualizar una inscripción por ID.
- `DELETE /inscriptions/{id}/`: Eliminar una inscripción por ID.

Ejemplo de solicitud para crear una inscripción:

```json
{
    'student_id': 1,
    'inscriptions': [
        {'subject_id': 1, 'calification': 3.5}
    ]
}
```

La calificación es opcional en este caso.

Si todo esta bien responderá un mensaje de éxito: `"Inscriptions created successfully"`.


## Documentación

La documentación de la API está disponible en `/docs/` utilizando Swagger.

## Base de datos

La base de datos tiene las siguientes tablas:

- `students`: Datos de los estudiantes.
- `teachers`: datos de los profesores.
- `subjects`: Datos de las materias.
- `inscriptions`: Datos de las inscripciones.
- `users`: Datos de los usuarios que usa el modelo que ya existe en Django.

Hice un diagrama de la base de datos para ayudar a entender las relaciones aunque hay una tabla extra para la relacion de materia consigo misma:



## Licencia

Este proyecto está bajo la licencia MIT.
