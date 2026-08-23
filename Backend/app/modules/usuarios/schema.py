from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict
from app.modules.roles.schema import RolResponse

class UsuarioCreate(BaseModel):
    """
    Datos necesarios para registrar un nuevo usuario.
    El idUsuario NO se recibe porque se genera automáticamente.
    """

    nombres: str
    apellidos: str
    numeroDocumento: str
    tipoDocumento: str
    correoElectronico: EmailStr
    telefono: str
    password: str


class UsuarioUpdate(BaseModel):
    """
    Datos permitidos para actualizar un usuario.
    Todos los campos son opcionales.
    """

    nombres: str | None = None
    apellidos: str | None = None
    numeroDocumento: str | None = None
    tipoDocumento: str | None = None
    correoElectronico: EmailStr | None = None
    telefono: str | None = None


class UsuarioResponse(BaseModel):
    """
    Información pública del usuario.
    Nunca incluye la contraseña.
    """

    idUsuario: UUID
    nombres: str
    apellidos: str
    numeroDocumento: str
    tipoDocumento: str
    correoElectronico: EmailStr
    telefono: str
    estado: bool

    model_config = ConfigDict(from_attributes=True)

class UsuarioConRolesResponse(UsuarioResponse):
    """
    Usuario acompañado de sus roles.
    """

    roles: list[RolResponse] = []
