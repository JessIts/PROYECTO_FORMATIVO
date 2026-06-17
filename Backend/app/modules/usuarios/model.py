from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    idUsuario = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    estado = Column(
        Enum(
            "activo",
            "inactivo",
            name="estado_usuario"
        ),
        default="activo"
    )

    fechaRegistro = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    roles = relationship(
    "Rol",
    secondary="usuario_rol",
    back_populates="usuarios"
)