from uuid import UUID

from pydantic import BaseModel, ConfigDict


# ============================================================
# ASIGNAR ROL A USUARIO
# ============================================================

class UsuarioRolCreate(BaseModel):
    idUsuario: UUID
    idRol: UUID


# ============================================================
# RESPUESTA
# ============================================================

class UsuarioRolResponse(BaseModel):
    idUsuario: UUID
    idRol: UUID

    model_config = ConfigDict(
        from_attributes=True
    )