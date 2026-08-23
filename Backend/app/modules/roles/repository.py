from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.roles.model import Rol


class RolRepository:

    # ============================================================
    # CREAR
    # ============================================================

    @staticmethod
    def crear(
        db: Session,
        rol: Rol
    ) -> Rol:

        db.add(rol)
        db.commit()
        db.refresh(rol)

        return rol

    # ============================================================
    # OBTENER POR ID
    # ============================================================

    @staticmethod
    def obtener_por_id(
        db: Session,
        idRol: UUID
    ) -> Rol | None:

        return (
            db.query(Rol)
            .filter(
                Rol.idRol == idRol
            )
            .first()
        )

    # ============================================================
    # OBTENER POR NOMBRE
    # ============================================================

    @staticmethod
    def obtener_por_nombre(
        db: Session,
        nombre: str
    ) -> Rol | None:

        return (
            db.query(Rol)
            .filter(
                Rol.nombre == nombre
            )
            .first()
        )

    # ============================================================
    # OBTENER TODOS
    # ============================================================

    @staticmethod
    def obtener_todos(
        db: Session
    ) -> list[Rol]:

        return (
            db.query(Rol)
            .all()
        )

    # ============================================================
    # ACTUALIZAR
    # ============================================================

    @staticmethod
    def actualizar(
        db: Session,
        rol: Rol
    ) -> Rol:

        db.commit()
        db.refresh(rol)

        return rol

    # ============================================================
    # ELIMINAR
    # ============================================================

    @staticmethod
    def eliminar(
        db: Session,
        idRol: UUID
    ) -> bool:

        rol = (
            RolRepository.obtener_por_id(
                db,
                idRol
            )
        )

        if rol is None:
            return False

        db.delete(rol)
        db.commit()

        return True