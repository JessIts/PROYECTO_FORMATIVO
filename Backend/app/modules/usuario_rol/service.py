from app.modules.usuario_rol.model import UsuarioRol
from app.modules.usuario_rol.repository import UsuarioRolRepository

from app.modules.usuarios.repository import UsuarioRepository
from app.modules.roles.repository import RolRepository


class UsuarioRolService:

    @staticmethod
    def asignar(
        db,
        id_usuario,
        id_rol
    ):

        usuario = UsuarioRepository.obtener_por_id(
            db,
            id_usuario
        )

        if not usuario:
            return "USUARIO_NO_EXISTE"

        rol = RolRepository.obtener_por_id(
            db,
            id_rol
        )

        if not rol:
            return "ROL_NO_EXISTE"

        relacion = UsuarioRolRepository.obtener(
            db,
            id_usuario,
            id_rol
        )

        if relacion:
            return "YA_EXISTE"

        nueva_relacion = UsuarioRol(
            idUsuario=id_usuario,
            idRol=id_rol
        )

        return UsuarioRolRepository.crear(
            db,
            nueva_relacion
        )
        
    @staticmethod
    def remover(
        db,
        id_usuario,
        id_rol
    ):

        relacion = UsuarioRolRepository.obtener(
            db,
            id_usuario,
            id_rol
        )

        if not relacion:
            return False

        UsuarioRolRepository.eliminar(
            db,
            relacion
        )

        return True

    @staticmethod
    def obtener_roles_usuario(
        db,
        id_usuario
    ):

        usuario = UsuarioRepository.obtener_por_id(
            db,
            id_usuario
        )

        if not usuario:
            return None

        return usuario.roles