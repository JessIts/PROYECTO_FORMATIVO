from pydantic import BaseModel


class RolBase(BaseModel):
    nombre: str


class RolCreate(RolBase):
    pass


class RolUpdate(RolBase):
    pass


class RolResponse(RolBase):
    idRol: int

    class Config:
        from_attributes = True