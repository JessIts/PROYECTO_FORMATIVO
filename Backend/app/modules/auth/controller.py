# ============================================================
# app/modules/auth/controller.py
# ============================================================

from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.auth.service import AuthService
from app.modules.auth.password_service import PasswordService
from app.modules.auth.schema import LoginRequest


class AuthController:

    # ========================================================
    # LOGIN
    # ========================================================

    @staticmethod
    def login(
        db: Session,
        data: LoginRequest
    ):
        return AuthService.login(
            db,
            data.correoElectronico,
            data.password
        )


    # ========================================================
    # USUARIO AUTENTICADO
    # ========================================================

    @staticmethod
    def obtener_usuario_actual(
        db: Session,
        id_usuario: UUID
    ):
        return AuthService.obtener_usuario_actual(
            db,
            id_usuario
        )


    # ========================================================
    # RECUPERACIÓN DE CONTRASEÑA
    # ========================================================

    @staticmethod
    def forgot_password(
        db: Session,
        correoElectronico: str
    ):
        return PasswordService.solicitar_recuperacion(
            db,
            correoElectronico
        )


    # ========================================================
    # RESTABLECER CONTRASEÑA
    # ========================================================

    @staticmethod
    def reset_password(
        db: Session,
        token: str,
        nueva_password: str
    ):
        return PasswordService.restablecer_password(
            db,
            token,
            nueva_password
        )