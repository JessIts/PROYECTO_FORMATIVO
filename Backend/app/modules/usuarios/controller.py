from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.modules.usuarios.schema import (
    UsuarioCreate,
    UsuarioResponse,
    UsuarioUpdate
)

from app.modules.usuarios.service import UsuarioService


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


# ============================================================
# CREAR USUARIO
# ============================================================

@router.post(
    "/",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_usuario(
    data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    try:
        return UsuarioService.registrar_usuario(
            db,
            data
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# ============================================================
# OBTENER TODOS LOS USUARIOS
# ============================================================

@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def obtener_usuarios(
    db: Session = Depends(get_db)
):
    return UsuarioService.obtener_usuarios(
        db
    )


# ============================================================
# OBTENER USUARIO POR UUID
# ============================================================

@router.get(
    "/{id_usuario}",
    response_model=UsuarioResponse
)
def obtener_usuario(
    id_usuario: UUID,
    db: Session = Depends(get_db)
):
    usuario = UsuarioService.obtener_usuario(
        db,
        id_usuario
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario


# ============================================================
# ACTUALIZAR USUARIO
# ============================================================

@router.put(
    "/{id_usuario}",
    response_model=UsuarioResponse
)
def actualizar_usuario(
    id_usuario: UUID,
    data: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    try:
        usuario = UsuarioService.actualizar_usuario(
            db,
            id_usuario,
            data
        )

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )

        return usuario

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# ============================================================
# ELIMINAR USUARIO
# ============================================================

@router.delete(
    "/{id_usuario}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_usuario(
    id_usuario: UUID,
    db: Session = Depends(get_db)
):
    eliminado = UsuarioService.eliminar_usuario(
        db,
        id_usuario
    )

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return None