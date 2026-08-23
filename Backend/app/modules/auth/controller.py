# ============================================================
# app/modules/auth/controller.py
# ============================================================

from sqlalchemy.orm import Session

from app.modules.auth.service import AuthService
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