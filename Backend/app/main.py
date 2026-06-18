from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.modules.usuarios.routes import router as usuarios_router
from app.modules.roles.routes import router as rol_router
from app.modules.usuario_rol.routes import router as usuario_rol_router
from app.modules.usuarios.model import Usuario
from app.modules.roles.model import Rol
from app.modules.usuario_rol.model import UsuarioRol
from app.modules.auth.routes import router as auth_router
from app.modules.auth.password_token_model import PasswordResetToken

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Sistema SIHS"
)

app.include_router(
    usuarios_router
)

app.include_router(
    auth_router
)

app.include_router(
    rol_router
)

app.include_router(
    usuario_rol_router
)