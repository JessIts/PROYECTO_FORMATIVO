from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.usuario_rol.model import UsuarioRol
from app.modules.roles.model import Rol


class UsuarioRolRepository:

    # ============================================================
    # CREAR RELACIÓN
    # ============================================================

    @staticmethod
    def crear(
        db: Session,
        usuario_rol: UsuarioRol
    ) -> UsuarioRol:

        db.add(usuario_rol)
        db.commit()
        db.refresh(usuario_rol)

        return usuario_rol

    # ============================================================
    # BUSCAR RELACIÓN
    # ============================================================

    @staticmethod
    def obtener_relacion(
        db: Session,
        id_usuario: UUID,
        id_rol: UUID
    ) -> UsuarioRol | None:

        return (
            db.query(UsuarioRol)
            .filter(
                UsuarioRol.idUsuario == id_usuario,
                UsuarioRol.idRol == id_rol
            )
            .first()
        )

    # ============================================================
    # OBTENER RELACIONES DE UN USUARIO
    # ============================================================

    @staticmethod
    def obtener_roles_usuario(
        db: Session,
        id_usuario: UUID
    ) -> list[UsuarioRol]:

        return (
            db.query(UsuarioRol)
            .filter(
                UsuarioRol.idUsuario == id_usuario
            )
            .all()
        )

    # ============================================================
    # OBTENER ROLES DE UN USUARIO
    # ============================================================

    @staticmethod
    def obtener_roles_por_usuario(
        db: Session,
        id_usuario: UUID
    ) -> list[Rol]:

        return (
            db.query(Rol)
            .join(
                UsuarioRol,
                UsuarioRol.idRol == Rol.idRol
            )
            .filter(
                UsuarioRol.idUsuario == id_usuario
            )
            .all()
        )

    # ============================================================
    # OBTENER USUARIOS DE UN ROL
    # ============================================================

    @staticmethod
    def obtener_usuarios_rol(
        db: Session,
        id_rol: UUID
    ) -> list[UsuarioRol]:

        return (
            db.query(UsuarioRol)
            .filter(
                UsuarioRol.idRol == id_rol
            )
            .all()
        )

    # ============================================================
    # ELIMINAR RELACIÓN
    # ============================================================

    @staticmethod
    def eliminar_rol(
        db: Session,
        id_usuario: UUID,
        id_rol: UUID
    ) -> bool:

        usuario_rol = UsuarioRolRepository.obtener_relacion(
            db=db,
            id_usuario=id_usuario,
            id_rol=id_rol
        )

        if usuario_rol is None:
            return False

        db.delete(usuario_rol)
        db.commit()

        return True