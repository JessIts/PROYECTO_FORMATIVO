# ============================================================
# app/main.py
# ============================================================

from fastapi import FastAPI


# ============================================================
# BASE DE DATOS
# ============================================================

# ------------------------------------------------------------
# Base contiene el metadata de todos nuestros modelos
# SQLAlchemy.
# ------------------------------------------------------------

from app.database.base import Base

# ------------------------------------------------------------
# engine representa la conexión configurada hacia PostgreSQL.
# ------------------------------------------------------------

from app.database.connection import engine


# ============================================================
# MODELOS
# ============================================================

# ------------------------------------------------------------
# Importamos los modelos para que SQLAlchemy los registre
# dentro de Base.metadata.
#
# IMPORTANTE:
# Estos modelos ya deben estar refactorizados para utilizar
# UUID donde corresponda.
# ------------------------------------------------------------

from app.modules.usuarios.model import Usuario
from app.modules.roles.model import Rol
from app.modules.usuario_rol.model import UsuarioRol

# ------------------------------------------------------------
# Modelo utilizado para los tokens de recuperación de
# contraseña.
# ------------------------------------------------------------

from app.modules.auth.password_token_model import PasswordResetToken


# ============================================================
# ROUTERS
# ============================================================

# ------------------------------------------------------------
# Usuarios
# ------------------------------------------------------------

from app.modules.usuarios.routes import (
    router as usuarios_router
)

# ------------------------------------------------------------
# Autenticación
# ------------------------------------------------------------

from app.modules.auth.routes import (
    router as auth_router
)

# ------------------------------------------------------------
# Roles
# ------------------------------------------------------------

from app.modules.roles.routes import (
    router as rol_router
)

# ------------------------------------------------------------
# Relación Usuario - Rol
# ------------------------------------------------------------

from app.modules.usuario_rol.routes import (
    router as usuario_rol_router
)

# ============================================================
# IMPORTACION DE CORS
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# ============================================================
# CREACIÓN DE TABLAS
# ============================================================

# ------------------------------------------------------------
# create_all() crea las tablas que estén registradas en
# Base.metadata y que todavía no existan en la base de datos.
#
# IMPORTANTE:
#
# create_all() NO modifica automáticamente una tabla existente.
#
# Por ejemplo, si antes tenías:
#
#     idUsuario INTEGER
#
# y ahora cambiaste el modelo a:
#
#     idUsuario UUID
#
# create_all() NO convierte INTEGER → UUID.
#
# Para una base de datos existente necesitarías una migración
# (por ejemplo, Alembic) o recrear las tablas.
# ------------------------------------------------------------

Base.metadata.create_all(
    bind=engine
)


# ============================================================
# APLICACIÓN FASTAPI
# ============================================================

app = FastAPI(
    title="Sistema SIHS"
)

# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------
# Endpoints de usuarios
# ------------------------------------------------------------

app.include_router(
    usuarios_router
)


# ------------------------------------------------------------
# Endpoints de autenticación:
#
#     /auth/login
#     /auth/me
#     recuperación de contraseña
#     etc.
# ------------------------------------------------------------

app.include_router(
    auth_router
)


# ------------------------------------------------------------
# Endpoints de roles
# ------------------------------------------------------------

app.include_router(
    rol_router
)


# ------------------------------------------------------------
# Endpoints de relación Usuario - Rol
# ------------------------------------------------------------

app.include_router(
    usuario_rol_router
)