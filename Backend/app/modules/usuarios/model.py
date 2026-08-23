import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    idUsuario = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    nombres = Column(
        String(100),
        nullable=False
    )

    apellidos = Column(
        String(100),
        nullable=False
    )

    numeroDocumento = Column(
        String(30),
        nullable=False,
        unique=True,
        index=True
    )

    tipoDocumento = Column(
        String(20),
        nullable=False
    )

    correoElectronico = Column(
        String(150),
        nullable=False,
        unique=True,
        index=True
    )

    telefono = Column(
        String(20),
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    estado = Column(
        Boolean,
        nullable=False,
        default=True
    )

    roles = relationship(
        "Rol",
        secondary="usuario_rol",
        back_populates="usuarios"
    )