from sqlalchemy.orm import Session

from .model import Usuario

from sqlalchemy import text


class UsuarioRepository:

    @staticmethod
    def obtener_todos(db: Session):
        return db.query(Usuario).all()

    @staticmethod
    def obtener_por_id(
        db: Session,
        id_usuario: int
    ):
        return (
            db.query(Usuario)
            .filter(
                Usuario.idUsuario == id_usuario
            )
            .first()
        )

    @staticmethod
    def obtener_por_email(
        db: Session,
        email: str
    ):
        return (
            db.query(Usuario)
            .filter(
                Usuario.email == email
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        usuario: Usuario
    ):
        db.add(usuario)

        db.commit()

        db.refresh(usuario)

        return usuario
    
    @staticmethod
    def obtener_por_id(
    db: Session,
    id_usuario: int
    ):

        return (
        db.query(Usuario)
        .filter(
            Usuario.idUsuario == id_usuario
        )
        .first()
    )