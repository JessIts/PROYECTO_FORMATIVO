from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.usuario_rol.model import UsuarioRol


class UsuarioRolRepository:

    # ============================================================
    # CREAR
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
    # OBTENER ROLES DE USUARIO
    # ============================================================

    @staticmethod
    def obtener_roles_usuario(
        db: Session,
        id_usuario: UUID
    ):

        return (
            db.query(UsuarioRol)
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
    ):

        return (
            db.query(UsuarioRol)
            .filter(
                UsuarioRol.idRol == id_rol
            )
            .all()
        )

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
    # ELIMINAR
    # ============================================================

    @staticmethod
    def eliminar(
        db: Session,
        id_usuario: UUID,
        id_rol: UUID
    ) -> bool:

        usuario_rol = (
            UsuarioRolRepository.obtener_relacion(
                db,
                id_usuario,
                id_rol
            )
        )

        if usuario_rol is None:
            return False

        db.delete(usuario_rol)
        db.commit()

        return True