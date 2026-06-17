from fastapi import HTTPException

from app.modules.roles.service import RolService


class RolController:

    @staticmethod
    def obtener_todos(db):
        return RolService.obtener_todos(db)

    @staticmethod
    def obtener_por_id(
        db,
        id_rol
    ):
        rol = RolService.obtener_por_id(
            db,
            id_rol
        )

        if not rol:
            raise HTTPException(
                status_code=404,
                detail="Rol no encontrado"
            )

        return rol

    @staticmethod
    def crear(
        db,
        data
    ):
        return RolService.crear(
            db,
            data
        )

    @staticmethod
    def actualizar(
        db,
        id_rol,
        data
    ):
        rol = RolService.actualizar(
            db,
            id_rol,
            data
        )

        if not rol:
            raise HTTPException(
                status_code=404,
                detail="Rol no encontrado"
            )

        return rol

    @staticmethod
    def eliminar(
        db,
        id_rol
    ):
        eliminado = RolService.eliminar(
            db,
            id_rol
        )

        if not eliminado:
            raise HTTPException(
                status_code=404,
                detail="Rol no encontrado"
            )

        return {
            "mensaje": "Rol eliminado"
        }