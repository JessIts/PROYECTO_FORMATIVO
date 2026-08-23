# ============================================================
# app/modules/auth/service.py
# ============================================================

from sqlalchemy.orm import Session

from app.modules.usuarios.repository import UsuarioRepository

from app.core.security import (
    verify_password,
    create_access_token,
    hash_password
)


class AuthService:

    # ========================================================
    # LOGIN
    # ========================================================

    @staticmethod
    def login(
        db: Session,
        correoElectronico: str,
        password: str
    ):
        """
        Autentica un usuario y genera un JWT.
        """

        # ----------------------------------------------------
        # Buscar usuario por correo
        # ----------------------------------------------------

        usuario = UsuarioRepository.obtener_por_email(
            db,
            correoElectronico
        )

        # ----------------------------------------------------
        # Usuario inexistente
        # ----------------------------------------------------

        if not usuario:
            raise ValueError(
                "Credenciales incorrectas"
            )

        # ----------------------------------------------------
        # Usuario inactivo
        # ----------------------------------------------------

        if not usuario.estado:
            raise ValueError(
                "El usuario se encuentra inactivo"
            )

        # ----------------------------------------------------
        # Verificar contraseña
        # ----------------------------------------------------

        if not verify_password(
            password,
            usuario.password
        ):
            raise ValueError(
                "Credenciales incorrectas"
            )

        # ----------------------------------------------------
        # Crear JWT
        # ----------------------------------------------------

        token = create_access_token(
            data={
                # UUID convertido a string para el JWT
                "sub": str(usuario.idUsuario)
            }
        )

        # ----------------------------------------------------
        # Respuesta
        # ----------------------------------------------------

        return {
            "access_token": token,
            "token_type": "bearer"
        }