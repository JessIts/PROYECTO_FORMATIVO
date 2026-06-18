# Sistema SIHS - Backend

Backend desarrollado con **FastAPI**, **SQLAlchemy** y **PostgreSQL** siguiendo una arquitectura por capas para la gestión académica del Sistema Integrado de Horarios (SIHS).

## Tecnologías

* Python 3.12
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* JWT (JSON Web Tokens)
* Passlib (Hash de contraseñas)
* Uvicorn

---

# Arquitectura del Proyecto

```text
app/
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
│
├── database/
│   ├── base.py
│   └── connection.py
│
├── modules/
│   ├── auth/
│   ├── usuarios/
│   ├── roles/
│   └── usuario_rol/
│
└── main.py
```

Cada módulo sigue una arquitectura por capas:

```text
routes
   ↓
controller
   ↓
service
   ↓
repository
   ↓
database
```

---

# Funcionalidades Implementadas

## Gestión de Usuarios

* Crear usuario
* Listar usuarios
* Consultar usuario por ID
* Actualizar usuario
* Eliminar usuario

### Tabla

```sql
usuarios
```

---

## Seguridad

### Hash de Contraseñas

Las contraseñas se almacenan utilizando:

```python
bcrypt
```

Nunca se almacenan contraseñas en texto plano.

---

## Autenticación JWT

### Login

```http
POST /auth/login
```

Genera un token JWT para usuarios autenticados.

Ejemplo de respuesta:

```json
{
    "access_token": "jwt_token",
    "token_type": "bearer"
}
```

---

## Usuario Autenticado

### Obtener Usuario Actual

```http
GET /auth/me
```

Retorna la información del usuario asociado al token enviado.

---

# Roles y Permisos

## CRUD de Roles

Endpoints disponibles:

```http
GET    /roles
GET    /roles/{id}
POST   /roles
PUT    /roles/{id}
DELETE /roles/{id}
```

### Tabla

```sql
roles
```

---

## Relación Usuario - Rol

Se implementó una relación muchos a muchos mediante:

```sql
usuario_rol
```

---

## Asignar Rol a Usuario

```http
POST /usuario-rol/asignar
```

Body:

```json
{
    "idUsuario": 1,
    "idRol": 1
}
```

---

## Remover Rol

```http
DELETE /usuario-rol/remover
```

Body:

```json
{
    "idUsuario": 1,
    "idRol": 1
}
```

---

## Consultar Roles de un Usuario

```http
GET /usuario-rol/usuario/{id}
```

Respuesta:

```json
[
    {
        "idRol": 1,
        "nombre": "Administrador"
    }
]
```

---

# Autorización

Se implementó autorización basada en roles.

### Dependencias

```python
get_current_user()
```

Obtiene el usuario autenticado desde el JWT.

```python
require_admin()
```

Permite acceso únicamente a usuarios con rol Administrador.

Ejemplo:

```python
@router.get("/admin-test")
def admin_test(
    usuario=Depends(require_admin)
):
    return {"mensaje": "Acceso permitido"}
```

---

# Recuperación de Contraseña

Se implementó un flujo básico de recuperación de contraseña mediante tokens temporales.

### Tabla

```sql
password_reset_tokens
```

---

## Solicitar Recuperación

```http
POST /auth/forgot-password
```

Body:

```json
{
    "email": "usuario@email.com"
}
```

Respuesta:

```json
{
    "mensaje": "Token generado",
    "token": "TOKEN_GENERADO"
}
```

---

## Restablecer Contraseña

```http
POST /auth/reset-password
```

Body:

```json
{
    "token": "TOKEN_GENERADO",
    "nueva_password": "NuevaPassword123"
}
```

Respuesta:

```json
{
    "mensaje": "Contraseña actualizada"
}
```

---

# Base de Datos

Actualmente se encuentran implementadas las siguientes entidades:

* usuarios
* roles
* usuario_rol
* password_reset_tokens

---

# Ejecución del Proyecto

## Activar entorno virtual

Windows:

```bash
.venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---

## Documentación Swagger

```text
http://localhost:8000/docs
```

---

# Próximos Módulos

* Coordinaciones
* Programas
* Fichas
* Usuario_Ficha
* Trimestres
* Sedes
* Ambientes
* Jornadas
* Horarios
* Horario_Día
* Competencias
* Resultados de Aprendizaje
* Actividades de Aprendizaje

---

# Estado Actual

✅ CRUD Usuarios

✅ Autenticación JWT

✅ Hash de Contraseñas

✅ Recuperación de Contraseña

✅ CRUD Roles

✅ Asignación de Roles

✅ Autorización por Rol

✅ Arquitectura por Capas

🚧 Pendiente: Módulos académicos y programación de horarios
