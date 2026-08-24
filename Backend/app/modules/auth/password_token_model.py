from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base


class PasswordResetToken(Base):

    __tablename__ = "password_reset_tokens"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # SHA-256 del token enviado al usuario
    tokenHash = Column(
        String(64),
        unique=True,
        nullable=False,
        index=True
    )

    idUsuario = Column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.idUsuario"),
        nullable=False
    )

    usado = Column(
        Boolean,
        default=False,
        nullable=False
    )

    fechaExpiracion = Column(
        DateTime,
        nullable=False
    )