from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.core.dependencies import require_admin

from app.modules.usuario_rol.schema import (
    UsuarioRolCreate
)

from app.modules.usuario_rol.controller import (
    UsuarioRolController
)

from app.modules.usuario_rol.schema import (
    UsuarioRolResponse
)

router = APIRouter(
    prefix="/usuario-rol",
    tags=["Usuario Rol"]
)

@router.post("/asignar")
def asignar_rol(
    data: UsuarioRolCreate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.asignar(
        db,
        data
    )
    
@router.delete("/remover")
def remover_rol(
    data: UsuarioRolCreate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.remover(
        db,
        data
    )

@router.get(
    "/usuario/{id_usuario}",
    response_model=list[UsuarioRolResponse]
)
def obtener_roles_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.obtener_roles_usuario(
        db,
        id_usuario
    )