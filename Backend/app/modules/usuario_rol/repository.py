from sqlalchemy.orm import Session

from app.modules.usuario_rol.model import UsuarioRol


class UsuarioRolRepository:

    @staticmethod
    def obtener(
        db: Session,
        id_usuario: int,
        id_rol: int
    ):
        return (
            db.query(UsuarioRol)
            .filter(
                UsuarioRol.idUsuario == id_usuario,
                UsuarioRol.idRol == id_rol
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        relacion: UsuarioRol
    ):
        db.add(relacion)
        db.commit()
        db.refresh(relacion)

        return relacion

    @staticmethod
    def eliminar(
        db: Session,
        relacion: UsuarioRol
    ):
        db.delete(relacion)
        db.commit()
        
@staticmethod
def obtener_roles_usuario(
    db: Session,
    id_usuario: int
):
    return (
        db.query(UsuarioRol)
        .filter(
            UsuarioRol.idUsuario == id_usuario
        )
        .all()
    )