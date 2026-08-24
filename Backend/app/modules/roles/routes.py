from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.modules.roles.controller import RolController

from app.modules.roles.schema import (
    RolCreate,
    RolUpdate,
    RolResponse
)

from app.core.dependencies import require_admin


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


# ============================================================
# CREAR ROL
# ============================================================

@router.post(
    "/",
    response_model=RolResponse
)
def crear_rol(
    data: RolCreate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.crear(
        db,
        data
    )


# ============================================================
# OBTENER TODOS LOS ROLES
# ============================================================

@router.get(
    "/",
    response_model=list[RolResponse]
)
def obtener_roles(
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.obtener_todos(
        db
    )


# ============================================================
# ACTUALIZAR ROL
# ============================================================

@router.put(
    "/{id_rol}",
    response_model=RolResponse
)
def actualizar_rol(
    id_rol: UUID,
    data: RolUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.actualizar(
        db,
        id_rol,
        data
    )


# ============================================================
# ELIMINAR ROL
# ============================================================

@router.delete(
    "/{id_rol}"
)
def eliminar_rol(
    id_rol: UUID,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.eliminar(
        db,
        id_rol
    )