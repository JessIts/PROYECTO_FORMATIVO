from app.modules.usuarios.repository import UsuarioRepository
from app.modules.auth.password_token_model import PasswordResetToken
from app.core.security import (
    verify_password,
    create_access_token
)

from datetime import datetime
from datetime import timedelta

from app.core.security import (
    generate_reset_token,
    hash_password
)
from app.modules.auth.repository import (
    AuthRepository
)

class AuthService:

    @staticmethod
    def login(
        db,
        email,
        password
    ):
        print("EMAIL:", email)

        usuario = UsuarioRepository.obtener_por_email(
            db,
            email
        )

        print("USUARIO:", usuario)

        if usuario:
            print("HASH BD:", usuario.password)

        valido = verify_password(
            password,
            usuario.password
        )

        print("PASSWORD VALIDA:", valido)

        usuario = (
            UsuarioRepository.obtener_por_email(
                db,
                email
            )
        )

        if not usuario:
            raise Exception(
                "Credenciales inválidas"
            )

        valido = verify_password(
            password,
            usuario.password
        )

        if not valido:
            raise Exception(
                "Credenciales inválidas"
            )

        token = create_access_token(
            {
                "sub": str(
                    usuario.idUsuario
                )
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
        

    #servicio forgot password?
    @staticmethod
    def forgot_password(
        db,
        email
    ):

        usuario = (
            UsuarioRepository.obtener_por_email(
                db,
                email
            )
        )

        if not usuario:

            return

        token = generate_reset_token()

        expiration = (
            datetime.utcnow()
            + timedelta(hours=1)
        )

        reset_token = PasswordResetToken(
            token=token,
            idUsuario=usuario.idUsuario,
            fechaExpiracion=expiration
        )

        AuthRepository.guardar_token(
            db,
            reset_token
        )

        return token
    
    #servicio de reestablecimiento de contraseña
    @staticmethod
    def reset_password(
        db,
        token,
        nueva_password
    ):

        registro = (
            AuthRepository.obtener_token(
                db,
                token
            )
        )

        if not registro:
            raise Exception(
                "Token inválido"
            )

        if registro.usado:
            raise Exception(
                "Token ya utilizado"
            )

        if registro.fechaExpiracion < datetime.utcnow():
            raise Exception(
                "Token expirado"
            )

        usuario = (
            UsuarioRepository.obtener_por_id(
                db,
                registro.idUsuario
            )
        )

        usuario.password = hash_password(
            nueva_password
        )

        registro.usado = True

        db.commit()

        return True