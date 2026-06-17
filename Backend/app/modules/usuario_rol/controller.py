from fastapi import HTTPException

from app.modules.usuario_rol.service import (
    UsuarioRolService
)


class UsuarioRolController:

    @staticmethod
    def asignar(
        db,
        data
    ):

        resultado = UsuarioRolService.asignar(
            db,
            data.idUsuario,
            data.idRol
        )

        if resultado == "USUARIO_NO_EXISTE":
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        if resultado == "ROL_NO_EXISTE":
            raise HTTPException(
                status_code=404,
                detail="Rol no encontrado"
            )

        if resultado == "YA_EXISTE":
            raise HTTPException(
                status_code=400,
                detail="El usuario ya tiene ese rol"
            )

        return {
            "mensaje": "Rol asignado correctamente"
        }
        
    @staticmethod
    def remover(
        db,
         data
    ):

        eliminado = UsuarioRolService.remover(
            db,
            data.idUsuario,
            data.idRol
        )

        if not eliminado:
            raise HTTPException(
                status_code=404,
                detail="Relación no encontrada"
            )

        return {
            "mensaje": "Rol removido correctamente"
        }
    
    @staticmethod
    def obtener_roles_usuario(
        db,
        id_usuario
    ):

        roles = UsuarioRolService.obtener_roles_usuario(
            db,
            id_usuario
        )

        if roles is None:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return roles