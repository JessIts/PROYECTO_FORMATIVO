from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.modules.usuarios.schema import UsuarioResponse

from app.database.connection import get_db

from .controller import AuthController
from .schema import (
    LoginRequest,
    TokenResponse
)

from app.core.dependencies import (
    get_current_user
)

from app.core.dependencies import (require_admin)
from app.core.dependencies import require_roles


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    return AuthController.login(
        db,
        data
    )

@router.get(
    "/me",
    response_model=UsuarioResponse
)
def me(
    usuario=Depends(get_current_user)
):
    return usuario

@router.get("/admin-test")
def admin_test(
    usuario=Depends(require_admin)
):

    return {
        "mensaje": "Bienvenido administrador",
        "usuario": usuario.nombre
    }
