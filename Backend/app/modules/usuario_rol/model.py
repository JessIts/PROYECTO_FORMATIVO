from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base


class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    idUsuario = Column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.idUsuario"),
        primary_key=True
    )

    idRol = Column(
        UUID(as_uuid=True),
        ForeignKey("roles.idRol"),
        primary_key=True
    )