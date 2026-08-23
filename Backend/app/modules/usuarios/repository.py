from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.usuarios.model import Usuario


class UsuarioRepository:

    # ============================================================
    # CREAR
    # ============================================================

    @staticmethod
    def crear(
        db: Session,
        usuario: Usuario
    ) -> Usuario:

        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        return usuario

    # ============================================================
    # OBTENER POR ID
    # ============================================================

    @staticmethod
    def obtener_por_id(
        db: Session,
        idUsuario: UUID
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(
                Usuario.idUsuario == idUsuario
            )
            .first()
        )

    # ============================================================
    # OBTENER POR CORREO
    # ============================================================

    @staticmethod
    def obtener_por_email(
        db: Session,
        correoElectronico: str
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(
                Usuario.correoElectronico == correoElectronico
            )
            .first()
        )

    # ============================================================
    # OBTENER POR DOCUMENTO
    # ============================================================

    @staticmethod
    def obtener_por_documento(
        db: Session,
        numeroDocumento: str
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(
                Usuario.numeroDocumento == numeroDocumento
            )
            .first()
        )

    # ============================================================
    # OBTENER TODOS
    # ============================================================

    @staticmethod
    def obtener_todos(
        db: Session
    ) -> list[Usuario]:

        return (
            db.query(Usuario)
            .all()
        )

    # ============================================================
    # ACTUALIZAR
    # ============================================================

    @staticmethod
    def actualizar(
        db: Session,
        usuario: Usuario
    ) -> Usuario:

        db.commit()
        db.refresh(usuario)

        return usuario

    # ============================================================
    # ACTUALIZAR PASSWORD
    # ============================================================

    @staticmethod
    def actualizar_password(
        db: Session,
        idUsuario: UUID,
        password: str
    ) -> Usuario | None:

        usuario = (
            UsuarioRepository.obtener_por_id(
                db,
                idUsuario
            )
        )

        if usuario is None:
            return None

        usuario.password = password

        db.commit()
        db.refresh(usuario)

        return usuario

    # ============================================================
    # CAMBIAR ESTADO
    # ============================================================

    @staticmethod
    def cambiar_estado(
        db: Session,
        idUsuario: UUID,
        estado: bool
    ) -> Usuario | None:

        usuario = (
            UsuarioRepository.obtener_por_id(
                db,
                idUsuario
            )
        )

        if usuario is None:
            return None

        usuario.estado = estado

        db.commit()
        db.refresh(usuario)

        return usuario

    # ============================================================
    # ELIMINAR
    # ============================================================

    @staticmethod
    def eliminar(
        db: Session,
        idUsuario: UUID
    ) -> bool:

        usuario = (
            UsuarioRepository.obtener_por_id(
                db,
                idUsuario
            )
        )

        if usuario is None:
            return False

        db.delete(usuario)
        db.commit()

        return True