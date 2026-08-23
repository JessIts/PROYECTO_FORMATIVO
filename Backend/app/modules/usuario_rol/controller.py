from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.usuario_rol.service import UsuarioRolService
from app.modules.usuario_rol.schema import UsuarioRolCreate


class UsuarioRolController:

    # ============================================================
    # ASIGNAR ROL A USUARIO
    # ============================================================

    @staticmethod
    def asignar_rol(
        db: Session,
        data: UsuarioRolCreate
    ):
        return UsuarioRolService.asignar_rol(
            db,
            data
        )

    # ============================================================
    # OBTENER ROLES DE UN USUARIO
    # ============================================================

    @staticmethod
    def obtener_roles_usuario(
        db: Session,
        id_usuario: UUID
    ):
        return UsuarioRolService.obtener_roles_usuario(
            db,
            id_usuario
        )

    # ============================================================
    # OBTENER USUARIOS DE UN ROL
    # ============================================================

    @staticmethod
    def obtener_usuarios_rol(
        db: Session,
        id_rol: UUID
    ):
        return UsuarioRolService.obtener_usuarios_rol(
            db,
            id_rol
        )

    # ============================================================
    # ELIMINAR ROL DE USUARIO
    # ============================================================

    @staticmethod
    def eliminar_rol(
        db: Session,
        id_usuario: UUID,
        id_rol: UUID
    ):
        return UsuarioRolService.eliminar_rol(
            db,
            id_usuario,
            id_rol
        )