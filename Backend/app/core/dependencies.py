from fastapi import (
    Depends,
    HTTPException,
    status
)

# ------------------------------------------------------------
# UUID
#
# Se utiliza para convertir el "sub" del JWT, que llega como
# string, nuevamente a un objeto UUID.
# ------------------------------------------------------------

from uuid import UUID


# ------------------------------------------------------------
# SQLAlchemy
# ------------------------------------------------------------

from sqlalchemy.orm import Session


# ------------------------------------------------------------
# Dependencia para obtener la conexión a la base de datos.
# ------------------------------------------------------------

from app.database.connection import get_db


# ------------------------------------------------------------
# Función encargada de decodificar y validar el JWT.
# ------------------------------------------------------------

from app.core.security import decode_token


# ------------------------------------------------------------
# Repositorio de usuarios.
# ------------------------------------------------------------

from app.modules.usuarios.repository import UsuarioRepository


# ------------------------------------------------------------
# HTTPBearer
#
# Permite obtener el token enviado mediante:
#
# Authorization: Bearer <token>
#
# FastAPI se encarga de extraer las credenciales.
# ------------------------------------------------------------

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)


# ============================================================
# CONFIGURACIÓN DE SEGURIDAD
# ============================================================

# ------------------------------------------------------------
# Instanciamos HTTPBearer.
#
# Esta dependencia será utilizada por get_current_user().
# ------------------------------------------------------------

security = HTTPBearer()


# ============================================================
# OBTENER USUARIO ACTUAL
# ============================================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """
    Obtiene el usuario autenticado a partir del JWT.

    Flujo:

        1. FastAPI obtiene el Bearer Token.
        2. Se extrae el token.
        3. Se decodifica y valida el JWT.
        4. Se obtiene el "sub".
        5. Se convierte el "sub" de string a UUID.
        6. Se busca el usuario en la base de datos.
        7. Se retorna el usuario.

    Esta función es utilizada por los endpoints que requieren
    autenticación.
    """

    # --------------------------------------------------------
    # Obtenemos el JWT enviado por el cliente.
    #
    # Ejemplo:
    #
    # Authorization: Bearer eyJhbGciOiJIUzI1Ni...
    #
    # credentials.credentials contiene únicamente el token.
    # --------------------------------------------------------

    token = credentials.credentials


    # --------------------------------------------------------
    # Decodificamos y validamos el JWT.
    #
    # decode_token() retorna:
    #
    #     payload -> si el token es válido
    #     None    -> si el token es inválido
    # --------------------------------------------------------

    payload = decode_token(token)


    # --------------------------------------------------------
    # Verificamos que el token haya podido ser validado.
    # --------------------------------------------------------

    if not payload:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )


    # ========================================================
    # OBTENER ID DEL USUARIO
    # ========================================================

    # --------------------------------------------------------
    # El ID del usuario se almacena en el claim "sub".
    #
    # Como estamos utilizando UUID, el JWT tendrá algo como:
    #
    # "sub":
    # "550e8400-e29b-41d4-a716-446655440000"
    #
    # Los datos del JWT llegan como strings.
    # --------------------------------------------------------

    user_id = payload.get("sub")


    # --------------------------------------------------------
    # Verificamos que el JWT tenga el claim "sub".
    # --------------------------------------------------------

    if not user_id:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )


    # ========================================================
    # CONVERTIR STRING A UUID
    # ========================================================

    # --------------------------------------------------------
    # El UUID fue guardado como string al generar el JWT:
    #
    #     str(usuario.idUsuario)
    #
    # Ahora debemos convertirlo nuevamente a UUID para poder
    # utilizarlo correctamente con SQLAlchemy/PostgreSQL.
    # --------------------------------------------------------

    try:

        user_id = UUID(user_id)

    except (ValueError, TypeError):

        # ----------------------------------------------------
        # Si el valor almacenado en "sub" no es un UUID válido,
        # el token no se considera válido.
        # ----------------------------------------------------

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ID de usuario inválido"
        )


    # ========================================================
    # BUSCAR USUARIO
    # ========================================================

    # --------------------------------------------------------
    # Buscamos el usuario utilizando su UUID.
    #
    # ANTES:
    #
    #     int(user_id)
    #
    # AHORA:
    #
    #     user_id
    #
    # porque user_id ya es un objeto UUID.
    # --------------------------------------------------------

    usuario = UsuarioRepository.obtener_por_id(
        db,
        user_id
    )


    # --------------------------------------------------------
    # Verificamos que el usuario exista.
    # --------------------------------------------------------

    if not usuario:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )


    # --------------------------------------------------------
    # Retornamos el usuario autenticado.
    #
    # FastAPI podrá inyectarlo automáticamente en los
    # endpoints que utilicen:
    #
    #     Depends(get_current_user)
    # --------------------------------------------------------

    return usuario


# ============================================================
# REQUERIR UN ROL ESPECÍFICO
# ============================================================

def require_role(role_name: str):
    """
    Crea una dependencia que permite verificar si el usuario
    tiene un rol específico.

    Ejemplo:

        require_role("Administrador")

    El UUID del rol no necesita ser utilizado aquí porque
    estamos comprobando el nombre del rol.
    """

    def role_checker(
        usuario=Depends(get_current_user)
    ):
        # ----------------------------------------------------
        # Recorremos los roles asociados al usuario.
        #
        # Verificamos si alguno coincide con el nombre
        # solicitado.
        # ----------------------------------------------------

        tiene_rol = any(
            rol.nombre == role_name
            for rol in usuario.roles
        )


        # ----------------------------------------------------
        # Si el usuario no tiene el rol requerido,
        # devolvemos 403 Forbidden.
        # ----------------------------------------------------

        if not tiene_rol:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No autorizado"
            )


        # ----------------------------------------------------
        # Si tiene el rol, devolvemos el usuario.
        # ----------------------------------------------------

        return usuario

    return role_checker


# ============================================================
# REQUERIR UNO DE VARIOS ROLES
# ============================================================

def require_roles(*roles_permitidos):
    """
    Permite especificar varios roles permitidos.

    Ejemplo:

        Depends(
            require_roles(
                "Administrador",
                "Coordinador"
            )
        )

    El usuario podrá acceder si tiene al menos uno de ellos.
    """

    def role_checker(
        usuario=Depends(get_current_user)
    ):

        # ----------------------------------------------------
        # Verificamos si alguno de los roles del usuario
        # se encuentra dentro de los roles permitidos.
        # ----------------------------------------------------

        tiene_rol = any(
            rol.nombre in roles_permitidos
            for rol in usuario.roles
        )


        # ----------------------------------------------------
        # Si no tiene ningún rol permitido, rechazamos
        # la solicitud.
        # ----------------------------------------------------

        if not tiene_rol:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No autorizado"
            )


        # ----------------------------------------------------
        # Si tiene un rol permitido, retornamos el usuario.
        # ----------------------------------------------------

        return usuario

    return role_checker


# ============================================================
# DEPENDENCIAS DE ROLES
# ============================================================

# ------------------------------------------------------------
# Cada una de estas variables representa una dependencia
# reutilizable para proteger endpoints.
# ------------------------------------------------------------

require_admin = require_role(
    "admin"
)

require_coordinador = require_role(
    "Coordinador"
)

require_instructor = require_role(
    "Instructor"
)

require_aprendiz = require_role(
    "Aprendiz"
)