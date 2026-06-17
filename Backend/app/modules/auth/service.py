from app.modules.usuarios.repository import UsuarioRepository

from app.core.security import (
    verify_password,
    create_access_token
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
        
