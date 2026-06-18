from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.core.security import decode_token

from app.modules.usuarios.repository import (
    UsuarioRepository
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from fastapi import HTTPException
from fastapi import status


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = decode_token(token)

    if not payload:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    user_id = payload.get("sub")

    if not user_id:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    usuario = UsuarioRepository.obtener_por_id(
        db,
        int(user_id)
    )

    if not usuario:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return usuario


def require_role(role_name: str):

    def role_checker(
        usuario=Depends(get_current_user)
    ):

        tiene_rol = any(
            rol.nombre == role_name
            for rol in usuario.roles
        )

        if not tiene_rol:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No autorizado"
            )

        return usuario

    return role_checker


def require_roles(*roles_permitidos):

    def role_checker(
        usuario=Depends(get_current_user)
    ):

        if not any(
            rol.nombre in roles_permitidos
            for rol in usuario.roles
        ):
            raise HTTPException(
                status_code=403,
                detail="No autorizado"
            )

        return usuario

    return role_checker





require_admin = require_role(
    "Administrador"
)

require_coordinador = require_role(
    "Coordinador"
)

require_instructor = require_role(
    "Instructor"
)

require_aprendiz = require_role(
    "Aprendiz"
)