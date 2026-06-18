from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from app.database.base import Base


class PasswordResetToken(Base):

    __tablename__ = "password_reset_tokens"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    token = Column(
        String(255),
        unique=True,
        nullable=False
    )

    idUsuario = Column(
        Integer,
        ForeignKey("usuarios.idUsuario"),
        nullable=False
    )

    usado = Column(
        Boolean,
        default=False
    )

    fechaExpiracion = Column(
        DateTime,
        nullable=False
    )