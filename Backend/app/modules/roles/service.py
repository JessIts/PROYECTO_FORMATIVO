from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.roles.model import Rol
from app.modules.roles.repository import RolRepository


class RolService:

    @staticmethod
    def obtener_todos(
        db: Session
    ):
        return RolRepository.obtener_todos(db)

    @staticmethod
    def obtener_por_id(
        db: Session,
        id_rol: UUID
    ):
        return RolRepository.obtener_por_id(
            db,
            id_rol
        )

    @staticmethod
    def crear(
        db: Session,
        data
    ):
        nuevo_rol = Rol(
            nombre=data.nombre
        )

        return RolRepository.crear(
            db,
            nuevo_rol
        )

    @staticmethod
    def actualizar(
        db: Session,
        id_rol: UUID,
        data
    ):
        rol = RolRepository.obtener_por_id(
            db,
            id_rol
        )

        if not rol:
            return None

        rol.nombre = data.nombre

        return RolRepository.actualizar(
            db,
            rol
        )

    @staticmethod
    def eliminar(
        db: Session,
        id_rol: UUID
    ) -> bool:

        rol = RolRepository.obtener_por_id(
            db,
            id_rol
        )

        if not rol:
            return False

        RolRepository.eliminar(
            db,
            rol
        )

        return True