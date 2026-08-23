# ============================================================
# app/modules/roles/controller.py
# ============================================================

from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.roles.service import RolService
from app.modules.roles.schema import (
    RolCreate,
    RolUpdate
)


class RolController:

    # ========================================================
    # OBTENER TODOS LOS ROLES
    # ========================================================

    @staticmethod
    def obtener_todos(
        db: Session
    ):

        return RolService.obtener_todos(
            db
        )

    # ========================================================
    # OBTENER ROL POR UUID
    # ========================================================

    @staticmethod
    def obtener_por_id(
        db: Session,
        idRol: UUID
    ):

        return RolService.obtener_por_id(
            db,
            idRol
        )

    # ========================================================
    # CREAR ROL
    # ========================================================

    @staticmethod
    def crear(
        db: Session,
        data: RolCreate
    ):

        return RolService.crear(
            db,
            data
        )

    # ========================================================
    # ACTUALIZAR ROL
    # ========================================================

    @staticmethod
    def actualizar(
        db: Session,
        idRol: UUID,
        data: RolUpdate
    ):

        return RolService.actualizar(
            db,
            idRol,
            data
        )

    # ========================================================
    # ELIMINAR ROL
    # ========================================================

    @staticmethod
    def eliminar(
        db: Session,
        idRol: UUID
    ):

        return RolService.eliminar(
            db,
            idRol
        )