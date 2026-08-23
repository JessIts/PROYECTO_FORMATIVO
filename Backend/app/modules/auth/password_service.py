from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.modules.usuarios.repository import UsuarioRepository
from app.modules.auth.repository import AuthRepository
from app.modules.auth.password_token_model import PasswordResetToken

from app.core.security import (
    generate_reset_token,
    hash_password
)


class PasswordService:

    @staticmethod
    def solicitar_recuperacion(
        db: Session,
        correoElectronico: str
    ):
        """
        Genera un token para recuperación de contraseña.
        """

        usuario = UsuarioRepository.obtener_por_email(
            db,
            correoElectronico
        )

        if not usuario:
            raise ValueError(
                "No existe un usuario con ese correo electrónico"
            )

        token = generate_reset_token()

        fecha_expiracion = (
            datetime.utcnow() + timedelta(minutes=30)
        )

        token_obj = PasswordResetToken(
            token=token,
            idUsuario=usuario.idUsuario,
            usado=False,
            fechaExpiracion=fecha_expiracion
        )

        return AuthRepository.guardar_token(
            db,
            token_obj
        )

    @staticmethod
    def validar_token(
        db: Session,
        token: str
    ):
        """
        Valida que el token exista, no haya sido utilizado
        y no esté expirado.
        """

        token_obj = AuthRepository.obtener_token(
            db,
            token
        )

        if not token_obj:
            raise ValueError(
                "El token de recuperación no es válido"
            )

        if token_obj.usado:
            raise ValueError(
                "El token de recuperación ya fue utilizado"
            )

        if token_obj.fechaExpiracion < datetime.utcnow():
            raise ValueError(
                "El token de recuperación ha expirado"
            )

        return token_obj

    @staticmethod
    def restablecer_password(
        db: Session,
        token: str,
        nueva_password: str
    ):
        """
        Cambia la contraseña utilizando un token válido.
        """

        token_obj = PasswordService.validar_token(
            db,
            token
        )

        usuario = UsuarioRepository.obtener_por_id(
            db,
            token_obj.idUsuario
        )

        if not usuario:
            raise ValueError(
                "El usuario asociado al token no existe"
            )

        usuario.password = hash_password(
            nueva_password
        )

        UsuarioRepository.actualizar(
            db,
            usuario
        )

        # Marcar el token como utilizado
        token_obj.usado = True

        AuthRepository.guardar_token(
            db,
            token_obj
        )

        return True