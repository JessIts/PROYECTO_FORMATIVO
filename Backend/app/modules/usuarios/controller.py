from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .service import UsuarioService
from .schema import UsuarioCreate

service = UsuarioService()

def crear_usuario(
    data: UsuarioCreate,
    db: Session
):
    try:
        return service.crear_usuario(
            db,
            data
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )