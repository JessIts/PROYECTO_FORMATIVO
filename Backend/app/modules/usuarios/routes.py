from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.connection import get_db

from app.modules.usuarios.controller import (
    crear_usuario,
    obtener_usuarios,
    obtener_usuario,
    actualizar_usuario,
    eliminar_usuario
)

from app.modules.usuarios.schema import (
    UsuarioCreate,
    UsuarioResponse,
    UsuarioUpdate
)


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


# ============================================================
# LISTAR USUARIOS
# ============================================================

@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):
    return obtener_usuarios(db)


# ============================================================
# CREAR USUARIO
# ============================================================

@router.post(
    "/",
    response_model=UsuarioResponse
)
def registrar_usuario(
    data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crear_usuario(
        data,
        db
    )


# ============================================================
# OBTENER USUARIO POR UUID
# ============================================================

@router.get(
    "/{id_usuario}",
    response_model=UsuarioResponse
)
def obtener_usuario_por_id(
    id_usuario: UUID,
    db: Session = Depends(get_db)
):
    return obtener_usuario(
        id_usuario,
        db
    )


# ============================================================
# ACTUALIZAR USUARIO
# ============================================================

@router.put(
    "/{id_usuario}",
    response_model=UsuarioResponse
)
def editar_usuario(
    id_usuario: UUID,
    data: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    return actualizar_usuario(
        id_usuario,
        data,
        db
    )


# ============================================================
# ELIMINAR USUARIO
# ============================================================

@router.delete(
    "/{id_usuario}"
)
def borrar_usuario(
    id_usuario: UUID,
    db: Session = Depends(get_db)
):
    return eliminar_usuario(
        id_usuario,
        db
    )