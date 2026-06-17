from sqlalchemy.orm import Session

from app.modules.roles.model import Rol


class RolRepository:

    @staticmethod
    def obtener_todos(db: Session):
        return db.query(Rol).all()

    @staticmethod
    def obtener_por_id(
        db: Session,
        id_rol: int
    ):
        return (
            db.query(Rol)
            .filter(Rol.idRol == id_rol)
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        rol: Rol
    ):
        db.add(rol)
        db.commit()
        db.refresh(rol)

        return rol

    @staticmethod
    def actualizar(
        db: Session,
        rol: Rol
    ):
        db.commit()
        db.refresh(rol)

        return rol

    @staticmethod
    def eliminar(
        db: Session,
        rol: Rol
    ):
        db.delete(rol)
        db.commit()