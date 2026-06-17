from app.modules.roles.model import Rol
from app.modules.roles.repository import RolRepository


class RolService:

    @staticmethod
    def obtener_todos(db):
        return RolRepository.obtener_todos(db)

    @staticmethod
    def obtener_por_id(
        db,
        id_rol
    ):
        return RolRepository.obtener_por_id(
            db,
            id_rol
        )

    @staticmethod
    def crear(
        db,
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
        db,
        id_rol,
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
        db,
        id_rol
    ):
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