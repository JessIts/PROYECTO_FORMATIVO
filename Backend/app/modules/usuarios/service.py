from .repository import UsuarioRepository
from .model import Usuario
from app.core.security import hash_password


class UsuarioService:

    @staticmethod
    def listar_usuarios(db):

        return UsuarioRepository.obtener_todos(
            db
        )

    @staticmethod
    def crear_usuario(
        db,
        data
    ):

        existe = (
            UsuarioRepository.obtener_por_email(
                db,
                data.email
            )
        )

        if existe:
            raise Exception(
                "El correo ya existe"
            )

        usuario = Usuario(
            nombre=data.nombre,
            email=data.email,
            password=hash_password(
                data.password
            )
        )

        return UsuarioRepository.crear(
            db,
            usuario
        )