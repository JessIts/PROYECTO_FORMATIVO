from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.usuario_rol.model import UsuarioRol
from app.modules.usuario_rol.repository import UsuarioRolRepository
from app.modules.usuario_rol.schema import UsuarioRolCreate


class UsuarioRolService:

    # ============================================================
    # ASIGNAR ROL
    # ============================================================

    @staticmethod
    def asignar_rol(
        db: Session,
        data: UsuarioRolCreate
    ):

        relacion_existente = (
            UsuarioRolRepository.obtener_relacion(
                db,
                data.idUsuario,
                data.idRol
            )
        )

        if relacion_existente:
            raise ValueError(
                "El usuario ya tiene asignado este rol"
            )

        usuario_rol = UsuarioRol(
            idUsuario=data.idUsuario,
            idRol=data.idRol
        )

        return UsuarioRolRepository.crear(
            db,
            usuario_rol
        )

    # ============================================================
    # OBTENER ROLES DEL USUARIO
    # ============================================================

    @staticmethod
    def obtener_roles_usuario(
        db: Session,
        id_usuario: UUID
    ):

        return UsuarioRolRepository.obtener_roles_usuario(
            db,
            id_usuario
        )

    # ============================================================
    # OBTENER USUARIOS DEL ROL
    # ============================================================

    @staticmethod
    def obtener_usuarios_rol(
        db: Session,
        id_rol: UUID
    ):

        return UsuarioRolRepository.obtener_usuarios_rol(
            db,
            id_rol
        )

    # ============================================================
    # ELIMINAR ROL
    # ============================================================

    @staticmethod
    def eliminar_rol(
        db: Session,
        id_usuario: UUID,
        id_rol: UUID
    ):

        return UsuarioRolRepository.eliminar_rol(
            db,
            id_usuario,
            id_rol
        )