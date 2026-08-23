from pydantic import BaseModel, ConfigDict

from uuid import UUID


class RolCreate(BaseModel):
    """
    Datos necesarios para crear un rol.

    El idRol NO se recibe porque se genera automáticamente.
    """

    nombre: str


class RolUpdate(BaseModel):
    """
    Datos permitidos para actualizar un rol.
    """

    nombre: str | None = None
    
class RolResponse(BaseModel):
    """
    Información pública de un rol.
    """

    idRol: UUID
    nombre: str

    model_config = ConfigDict(from_attributes=True)