# API de Gestión de Tareas (To-Do List)

Esta es una API RESTful desarrollada con Django y Django REST Framework como parte de una prueba técnica. La API permite a los usuarios registrarse, autenticarse y gestionar sus propias listas de tareas personales.

## Características Principales

*   **Autenticación JWT:** Sistema de autenticación seguro basado en tokens (JSON Web Tokens) usando `djangorestframework-simplejwt`.
*   **Gestión de Tareas (CRUD):** Endpoints completos para crear, leer, actualizar y eliminar tareas.
*   **Permisos a Nivel de Objeto:** Los usuarios solo pueden ver y modificar las tareas que han creado.
*   **Filtrado, Búsqueda y Ordenación:** La lista de tareas se puede filtrar por estado (`completed`), buscar por texto en el título o descripción, y ordenar por fecha de creación o título.
*   **Paginación:** Las respuestas de listado están paginadas.
*   **Validaciones Robustas:** Validación de datos de entrada, incluyendo la obligatoriedad y longitud mínima de campos.
*   **Documentación Automática de API:** Documentación interactiva generada con `drf-spectacular`, disponible a través de Swagger UI y ReDoc.
*   **Pruebas Unitarias y de Integración:** Cobertura de pruebas para modelos y endpoints para garantizar la fiabilidad del código.

## Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en un entorno de desarrollo local.

### Prerrequisitos

*   Python 3.10 o superior
*   `pip` (gestor de paquetes de Python)
*   (Opcional) Git

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias listadas en `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Aplicar Migraciones

Aplica las migraciones para crear las tablas en la base de datos.

```bash
python manage.py migrate
```

### 5. Crear un Superusuario (Opcional)

Esto te permitirá acceder al panel de administración de Django.

```bash
python manage.py createsuperuser
```
Sigue las instrucciones para crear un nombre de usuario y una contraseña.

### 6. Ejecutar el Servidor de Desarrollo

¡Listo! Inicia el servidor.

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.

---

## Uso de la API

La API está documentada y se puede probar interactivamente a través de Swagger UI.

*   **Documentación Swagger UI:** `http://127.0.0.1:8000/api/schema/swagger-ui/`
*   **Documentación ReDoc:** `http://127.0.0.1:8000/api/schema/redoc/`

### Flujo de Autenticación

1.  **Registro:** Envía una petición `POST` a `/api/auth/register/` con `username`, `password` y `password2`.
2.  **Login (Obtener Token):** Envía una petición `POST` a `/api/auth/token/` con tu `username` y `password`. La respuesta contendrá un `access_token` y un `refresh_token`.
3.  **Peticiones Autenticadas:** Para acceder a los endpoints protegidos, incluye el token de acceso en la cabecera de la petición:
    ```
    Authorization: Bearer <tu_access_token>
    ```

### Endpoints Principales

| Método | Endpoint                    | Descripción                                      |
| :----- | :-------------------------- | :----------------------------------------------- |
| `POST` | `/api/auth/register/`       | Registrar un nuevo usuario.                      |
| `POST` | `/api/auth/token/`          | Obtener un par de tokens JWT (login).            |
| `POST` | `/api/auth/token/refresh/`  | Refrescar un token de acceso expirado.           |
| `GET`  | `/api/tasks/`               | Listar las tareas del usuario autenticado.       |
| `POST` | `/api/tasks/`               | Crear una nueva tarea.                           |
| `GET`  | `/api/tasks/{id}/`          | Obtener los detalles de una tarea específica.    |
| `PUT`  | `/api/tasks/{id}/`          | Actualizar una tarea completa.                   |
| `PATCH`| `/api/tasks/{id}/`          | Actualizar parcialmente una tarea.               |
| `DELETE`| `/api/tasks/{id}/`          | Eliminar una tarea.                              |

---

## Ejecución de Pruebas

Para ejecutar el conjunto de pruebas y verificar la integridad del código, usa el siguiente comando:

```bash
python manage.py test
```

Esto ejecutará todas las pruebas unitarias y de integración definidas en el proyecto.