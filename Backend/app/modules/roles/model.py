from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.base import Base


class Rol(Base):

    __tablename__ = "roles"

    idRol = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(50),
        unique=True,
        nullable=False
    )

    usuarios = relationship(
        "Usuario",
        secondary="usuario_rol",
        back_populates="roles"
    )