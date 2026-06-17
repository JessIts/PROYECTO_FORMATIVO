from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.modules.roles.controller import RolController
from app.modules.roles.schema import (
    RolCreate,
    RolUpdate,
    RolResponse
)

from app.core.dependencies import (
    require_admin
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

#crea los roles

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

#obtiene todos los roles
@router.get(
    "/",
    response_model=list[RolResponse]
)
def obtener_roles(
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.obtener_todos(db)

#obtiene roles por id

@router.get(
    "/{id_rol}",
    response_model=RolResponse
)
def obtener_rol(
    id_rol: int,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.obtener_por_id(
        db,
        id_rol
    )
    
#actualiza los roles

@router.put(
    "/{id_rol}",
    response_model=RolResponse
)
def actualizar_rol(
    id_rol: int,
    data: RolUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.actualizar(
        db,
        id_rol,
        data
    )
    
#elimina los roles
@router.delete(
    "/{id_rol}"
)
def eliminar_rol(
    id_rol: int,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return RolController.eliminar(
        db,
        id_rol
    )