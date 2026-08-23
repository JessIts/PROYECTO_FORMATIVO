from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.core.dependencies import require_admin

from app.modules.usuario_rol.schema import (
    UsuarioRolCreate,
    UsuarioRolResponse
)

from app.modules.usuario_rol.controller import (
    UsuarioRolController
)


router = APIRouter(
    prefix="/usuario-rol",
    tags=["Usuario Rol"]
)


# ============================================================
# ASIGNAR ROL A USUARIO
# ============================================================

@router.post(
    "/asignar"
)
def asignar_rol(
    data: UsuarioRolCreate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.asignar(
        db,
        data
    )


# ============================================================
# REMOVER ROL DE USUARIO
# ============================================================

@router.delete(
    "/remover"
)
def remover_rol(
    data: UsuarioRolCreate,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.remover(
        db,
        data
    )


# ============================================================
# OBTENER ROLES DE UN USUARIO
# ============================================================

@router.get(
    "/usuario/{id_usuario}",
    response_model=list[UsuarioRolResponse]
)
def obtener_roles_usuario(
    id_usuario: UUID,
    db: Session = Depends(get_db),
    usuario=Depends(require_admin)
):
    return UsuarioRolController.obtener_roles_usuario(
        db,
        id_usuario
    )