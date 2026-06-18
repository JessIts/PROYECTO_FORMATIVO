from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str


class UsuarioResponse(BaseModel):
    nombre: str
    email: EmailStr
    estado: str
    fechaRegistro: datetime

    class Config:
        from_attributes = True