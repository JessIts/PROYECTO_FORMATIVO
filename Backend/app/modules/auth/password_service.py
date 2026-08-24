from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.modules.usuarios.repository import UsuarioRepository
from app.modules.auth.repository import AuthRepository
from app.modules.auth.password_token_model import PasswordResetToken

from app.core.email import enviar_correo_recuperacion
from app.core.config import FRONTEND_URL

from app.core.security import (
    generate_reset_token,
    hash_reset_token,
    hash_password
)


class PasswordService:

    # ============================================================
    # SOLICITAR RECUPERACIÓN DE CONTRASEÑA
    # ============================================================

    @staticmethod
    def solicitar_recuperacion(
        db: Session,
        correoElectronico: str
    ):

        # --------------------------------------------------------
        # Buscar usuario por correo
        # --------------------------------------------------------

        usuario = UsuarioRepository.obtener_por_email(
            db,
            correoElectronico
        )

        # --------------------------------------------------------
        # No revelar si el correo existe
        # --------------------------------------------------------

        if not usuario:
            return {
                "message": (
                    "Si el correo está registrado, "
                    "recibirás un enlace para "
                    "restablecer tu contraseña."
                )
            }

        # --------------------------------------------------------
        # Generar token original
        # --------------------------------------------------------

        token = generate_reset_token()

        # --------------------------------------------------------
        # Generar hash del token
        #
        # El token original NO se almacena en la BD.
        # --------------------------------------------------------

        token_hash = hash_reset_token(
            token
        )

        # --------------------------------------------------------
        # Establecer expiración
        #
        # El token será válido durante 30 minutos.
        # --------------------------------------------------------

        fecha_expiracion = (
            datetime.utcnow()
            + timedelta(minutes=30)
        )

        # --------------------------------------------------------
        # Crear registro del token
        # --------------------------------------------------------

        token_obj = PasswordResetToken(
            tokenHash=token_hash,
            idUsuario=usuario.idUsuario,
            usado=False,
            fechaExpiracion=fecha_expiracion
        )

        # --------------------------------------------------------
        # Guardar token en BD
        # --------------------------------------------------------

        AuthRepository.guardar_token(
            db,
            token_obj
        )

        # --------------------------------------------------------
        # Construir enlace de recuperación
        #
        # Ejemplo:
        #
        # http://localhost:5173/reset-password?token=ABC123
        # --------------------------------------------------------

        enlace = (
            f"{FRONTEND_URL}"
            f"/reset-password"
            f"?token={token}"
        )

        # --------------------------------------------------------
        # Enviar correo
        # --------------------------------------------------------

        enviar_correo_recuperacion(
            correo_destino=usuario.correoElectronico,
            enlace=enlace
        )

        # --------------------------------------------------------
        # Respuesta
        #
        # IMPORTANTE:
        # Nunca devolver el token al frontend.
        # --------------------------------------------------------

        return {
            "message": (
                "Si el correo está registrado, "
                "recibirás un enlace para "
                "restablecer tu contraseña."
            )
        }

    # ============================================================
    # VALIDAR TOKEN
    # ============================================================

    @staticmethod
    def validar_token(
        db: Session,
        token: str
    ):

        # --------------------------------------------------------
        # Convertir token recibido a SHA-256
        # --------------------------------------------------------

        token_hash = hash_reset_token(
            token
        )

        # --------------------------------------------------------
        # Buscar token por hash
        # --------------------------------------------------------

        token_obj = AuthRepository.obtener_token(
            db,
            token_hash
        )

        # --------------------------------------------------------
        # Token inexistente
        # --------------------------------------------------------

        if not token_obj:
            raise ValueError(
                "El token de recuperación no es válido"
            )

        # --------------------------------------------------------
        # Token ya utilizado
        # --------------------------------------------------------

        if token_obj.usado:
            raise ValueError(
                "El token de recuperación ya fue utilizado"
            )

        # --------------------------------------------------------
        # Token expirado
        # --------------------------------------------------------

        if token_obj.fechaExpiracion < datetime.utcnow():
            raise ValueError(
                "El token de recuperación ha expirado"
            )

        return token_obj

    # ============================================================
    # RESTABLECER CONTRASEÑA
    # ============================================================

    @staticmethod
    def restablecer_password(
        db: Session,
        token: str,
        nueva_password: str
    ):

        # --------------------------------------------------------
        # Validar token
        # --------------------------------------------------------

        token_obj = PasswordService.validar_token(
            db,
            token
        )

        # --------------------------------------------------------
        # Obtener usuario asociado
        # --------------------------------------------------------

        usuario = UsuarioRepository.obtener_por_id(
            db,
            token_obj.idUsuario
        )

        if not usuario:
            raise ValueError(
                "El usuario asociado al token no existe"
            )

        # --------------------------------------------------------
        # Generar nuevo hash de contraseña
        # --------------------------------------------------------

        usuario.password = hash_password(
            nueva_password
        )

        # --------------------------------------------------------
        # Actualizar usuario
        # --------------------------------------------------------

        UsuarioRepository.actualizar(
            db,
            usuario
        )

        # --------------------------------------------------------
        # Invalidar token
        #
        # Esto evita que pueda volver a utilizarse.
        # --------------------------------------------------------

        token_obj.usado = True

        AuthRepository.actualizar_token(
            db,
            token_obj
        )

        # --------------------------------------------------------
        # Respuesta
        # --------------------------------------------------------

        return {
            "message": (
                "Contraseña restablecida correctamente"
            )
        }