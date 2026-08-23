from sqlalchemy.orm import Session

from app.modules.usuarios.model import Usuario
from app.modules.usuarios.repository import UsuarioRepository
from app.modules.usuarios.schema import (
    UsuarioCreate,
    UsuarioUpdate
)
from app.core.security import hash_password


class UsuarioService:

    @staticmethod
    def registrar_usuario(
        db: Session,
        datos: UsuarioCreate
    ) -> Usuario:

        # Verificar si el correo ya existe
        usuario_existente = UsuarioRepository.obtener_por_email(
            db,
            datos.correoElectronico
        )

        if usuario_existente:
            raise ValueError(
                "El correo electrónico ya está registrado"
            )

        # Verificar si el documento ya existe
        documento_existente = UsuarioRepository.obtener_por_documento(
            db,
            datos.numeroDocumento
        )

        if documento_existente:
            raise ValueError(
                "El número de documento ya está registrado"
            )

        # Crear usuario
        usuario = Usuario(
            nombres=datos.nombres,
            apellidos=datos.apellidos,
            numeroDocumento=datos.numeroDocumento,
            tipoDocumento=datos.tipoDocumento,
            correoElectronico=datos.correoElectronico,
            telefono=datos.telefono,
            password=hash_password(datos.password),
            estado=True
        )

        return UsuarioRepository.crear(
            db,
            usuario
        )

    @staticmethod
    def obtener_usuario(
        db: Session,
        id_usuario
    ) -> Usuario | None:

        return UsuarioRepository.obtener_por_id(
            db,
            id_usuario
        )

    @staticmethod
    def obtener_usuarios(
        db: Session
    ) -> list[Usuario]:

        return UsuarioRepository.obtener_todos(
            db
        )

    @staticmethod
    def actualizar_usuario(
        db: Session,
        id_usuario,
        datos: UsuarioUpdate
    ) -> Usuario | None:

        usuario = UsuarioRepository.obtener_por_id(
            db,
            id_usuario
        )

        if not usuario:
            return None

        # Actualizar solamente los campos enviados
        if datos.nombres is not None:
            usuario.nombres = datos.nombres

        if datos.apellidos is not None:
            usuario.apellidos = datos.apellidos

        if datos.numeroDocumento is not None:
            # Verificar que el documento no pertenezca a otro usuario
            usuario_documento = (
                UsuarioRepository.obtener_por_documento(
                    db,
                    datos.numeroDocumento
                )
            )

            if (
                usuario_documento
                and usuario_documento.idUsuario != usuario.idUsuario
            ):
                raise ValueError(
                    "El número de documento ya está registrado"
                )

            usuario.numeroDocumento = datos.numeroDocumento

        if datos.tipoDocumento is not None:
            usuario.tipoDocumento = datos.tipoDocumento

        if datos.correoElectronico is not None:
            # Verificar que el correo no pertenezca a otro usuario
            usuario_correo = (
                UsuarioRepository.obtener_por_email(
                    db,
                    datos.correoElectronico
                )
            )

            if (
                usuario_correo
                and usuario_correo.idUsuario != usuario.idUsuario
            ):
                raise ValueError(
                    "El correo electrónico ya está registrado"
                )

            usuario.correoElectronico = datos.correoElectronico

        if datos.telefono is not None:
            usuario.telefono = datos.telefono

        if datos.estado is not None:
            usuario.estado = datos.estado

        return UsuarioRepository.actualizar(
            db,
            usuario
        )

    @staticmethod
    def eliminar_usuario(
        db: Session,
        id_usuario
    ) -> bool:

        usuario = UsuarioRepository.obtener_por_id(
            db,
            id_usuario
        )

        if not usuario:
            return False

        UsuarioRepository.eliminar(
            db,
            usuario
        )

        return True