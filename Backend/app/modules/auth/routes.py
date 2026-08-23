# ============================================================
# app/modules/auth/routes.py
# ============================================================

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


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
    UsuarioResponse
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
# USUARIO ACTUAL
# ============================================================

@router.get(
    "/me",
    response_model=UsuarioResponse
)
def me(
    usuario=Depends(get_current_user)
):

    return usuario


# ============================================================
# PRUEBA DE ADMINISTRADOR
# ============================================================

@router.get(
    "/admin-test"
)
def admin_test(
    usuario=Depends(require_admin)
):

    return {
        "mensaje": "Bienvenido administrador",
        "usuario": usuario.nombres
    }


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
        data
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
        data
    )