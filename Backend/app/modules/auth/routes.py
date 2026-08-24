from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.modules.usuarios.schema import (
    UsuarioResponse,
    UsuarioConRolesResponse
)

# ============================================================
# DATABASE
# ============================================================

from app.database.connection import get_db


# ============================================================
# DEPENDENCIAS
# ============================================================

from app.core.dependencies import (
    get_current_user,
    require_admin
)


# ============================================================
# CONTROLLER
# ============================================================

from app.modules.auth.controller import (
    AuthController
)


# ============================================================
# SCHEMAS
# ============================================================

from app.modules.auth.schema import (
    ForgotPasswordRequest,
    LoginRequest,
    ResetPasswordRequest,
    TokenResponse
)


# ============================================================
# USUARIO
# ============================================================

from app.modules.usuarios.schema import (
    UsuarioResponse,
    UsuarioConRolesResponse
)


# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


# ============================================================
# LOGIN
# ============================================================

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


# ============================================================
# USUARIO AUTENTICADO
# ============================================================

@router.get(
    "/me",
    response_model=UsuarioConRolesResponse
)
def obtener_usuario_actual(
    usuario=Depends(get_current_user)
):

    return usuario


# ============================================================
# SOLICITAR RECUPERACIÓN DE CONTRASEÑA
# ============================================================

@router.post(
    "/forgot-password"
)
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):

    return AuthController.forgot_password(
        db,
        data.correoElectronico
    )


# ============================================================
# RESTABLECER CONTRASEÑA
# ============================================================

@router.post(
    "/reset-password"
)
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):

    return AuthController.reset_password(
        db,
        data.token,
        data.nuevaPassword
    )