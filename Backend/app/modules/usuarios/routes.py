from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from .service import UsuarioService
from .schema import (
    UsuarioCreate,
    UsuarioResponse
)

from app.database.connection import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):
    return UsuarioService.listar_usuarios(db)


@router.post(
    "/",
    response_model=UsuarioResponse
)
def crear_usuario(
    data: UsuarioCreate,
    db: Session = Depends(get_db)
):

    try:
        return UsuarioService.crear_usuario(
            db,
            data
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
        