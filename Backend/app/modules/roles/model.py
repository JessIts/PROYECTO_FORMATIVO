import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base import Base


class Rol(Base):
    __tablename__ = "roles"

    idRol = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    nombre = Column(
        String(50),
        nullable=False,
        unique=True
    )

    usuarios = relationship(
        "Usuario",
        secondary="usuario_rol",
        back_populates="roles"
    )