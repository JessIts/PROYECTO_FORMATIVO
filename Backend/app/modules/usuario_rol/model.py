from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.base import Base


class UsuarioRol(Base):

    __tablename__ = "usuario_rol"

    idUsuario = Column(
        Integer,
        ForeignKey("usuarios.idUsuario"),
        primary_key=True
    )

    idRol = Column(
        Integer,
        ForeignKey("roles.idRol"),
        primary_key=True
    )