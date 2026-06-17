from pydantic import BaseModel


class UsuarioRolCreate(BaseModel):
    idUsuario: int
    idRol: int
    
class UsuarioRolResponse(BaseModel):
    idRol: int
    nombre: str

    class Config:
        from_attributes = True