from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.modules.auth.service import AuthService
from app.modules.usuarios.schema import UsuarioResponse

from app.database.connection import get_db

from .controller import AuthController
from .schema import (
    ForgotPasswordRequest,
    LoginRequest,
    ResetPasswordRequest,
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


@router.post(
    "/forgot-password"
)
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):

    token = AuthService.forgot_password(
        db,
        data.email
    )

    if not token:
        return {
            "mensaje":
            "Correo no encontrado"
        }

    return {
        "mensaje":
        "Token generado",
        "token": token
    }
    
    
@router.post(
    "/reset-password"
)
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):

    AuthService.reset_password(
        db,
        data.token,
        data.nueva_password
    )

    return {
        "mensaje":
        "Contraseña actualizada"
    }