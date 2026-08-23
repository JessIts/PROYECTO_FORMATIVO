# ============================================================
# app/core/security.py
# ============================================================

# ------------------------------------------------------------
# Importaciones para manejar fechas y tiempo de expiración
# ------------------------------------------------------------

from datetime import datetime, timedelta

# ------------------------------------------------------------
# secrets:
# Se utiliza para generar tokens seguros y aleatorios.
# En este caso, para recuperación de contraseña.
# ------------------------------------------------------------

import secrets

# ------------------------------------------------------------
# python-jose:
# jwt      -> Permite crear y decodificar tokens JWT.
# JWTError -> Permite capturar errores al validar un JWT.
# ------------------------------------------------------------

from jose import jwt, JWTError

# ------------------------------------------------------------
# Passlib:
# CryptContext permite trabajar con algoritmos de hash
# para almacenar y verificar contraseñas.
# ------------------------------------------------------------

from passlib.context import CryptContext

# ------------------------------------------------------------
# Configuración de JWT
#
# SECRET_KEY:
#   Clave secreta utilizada para firmar el JWT.
#
# ALGORITHM:
#   Algoritmo utilizado para firmar el token.
#
# ACCESS_TOKEN_EXPIRE_MINUTES:
#   Tiempo de vida del token de acceso.
# ------------------------------------------------------------

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)


# ============================================================
# CONFIGURACIÓN PARA CONTRASEÑAS
# ============================================================

# ------------------------------------------------------------
# Configuramos Passlib para utilizar bcrypt.
#
# bcrypt se utiliza únicamente para las contraseñas.
# No tiene relación con los UUID ni con el JWT.
# ------------------------------------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ============================================================
# HASH DE CONTRASEÑA
# ============================================================

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para una contraseña.

    La contraseña original nunca debería almacenarse
    directamente en la base de datos.

    Ejemplo:

        password:
            "123456"

        resultado:
            "$2b$12$..."
    """

    return pwd_context.hash(password)


# ============================================================
# VERIFICACIÓN DE CONTRASEÑA
# ============================================================

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Verifica si una contraseña ingresada coincide
    con el hash almacenado en la base de datos.

    Parámetros:
        plain_password:
            Contraseña que introduce el usuario.

        hashed_password:
            Hash almacenado en la base de datos.

    Retorna:
        True  -> La contraseña es correcta.
        False -> La contraseña es incorrecta.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ============================================================
# CREACIÓN DEL TOKEN JWT
# ============================================================

def create_access_token(data: dict) -> str:
    """
    Crea un token JWT.

    IMPORTANTE PARA UUID:
    --------------------------------------------
    Esta función no necesita convertir directamente
    el UUID.

    La conversión debe hacerse antes de llamar a esta
    función.

    Ejemplo:

        data={
            "sub": str(usuario.idUsuario)
        }

    De esta manera el UUID se almacena dentro del JWT
    como una cadena de texto.

    Ejemplo de UUID:

        550e8400-e29b-41d4-a716-446655440000

    """

    # --------------------------------------------------------
    # Copiamos los datos recibidos para no modificar
    # directamente el diccionario original.
    # --------------------------------------------------------

    payload = data.copy()

    # --------------------------------------------------------
    # Calculamos la fecha y hora de expiración del token.
    #
    # datetime.utcnow()
    #     Obtiene la fecha/hora actual en UTC.
    #
    # timedelta(...)
    #     Agrega los minutos configurados.
    # --------------------------------------------------------

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    # --------------------------------------------------------
    # Agregamos la fecha de expiración al payload.
    #
    # "exp" es un claim estándar de JWT.
    # --------------------------------------------------------

    payload.update({
        "exp": expire
    })

    # --------------------------------------------------------
    # Firmamos y generamos el JWT.
    #
    # SECRET_KEY:
    #     Clave utilizada para firmar el token.
    #
    # ALGORITHM:
    #     Algoritmo utilizado para la firma.
    # --------------------------------------------------------

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ============================================================
# DECODIFICACIÓN Y VALIDACIÓN DEL JWT
# ============================================================

def decode_token(token: str):
    """
    Decodifica y valida un token JWT.

    Si el token es válido:
        Retorna el payload.

    Si el token es inválido, está manipulado
    o expiró:
        Retorna None.
    """

    try:

        # ----------------------------------------------------
        # Decodificamos el token utilizando la misma clave
        # y algoritmo utilizados para crearlo.
        # ----------------------------------------------------

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # ----------------------------------------------------
        # Retornamos la información almacenada dentro
        # del JWT.
        # ----------------------------------------------------

        return payload

    except JWTError:

        # ----------------------------------------------------
        # Si ocurre cualquier error relacionado con JWT,
        # consideramos que el token no es válido.
        # ----------------------------------------------------

        return None


# ============================================================
# TOKEN DE RECUPERACIÓN DE CONTRASEÑA
# ============================================================

def generate_reset_token() -> str:
    """
    Genera un token seguro para recuperación de contraseña.

    Este token es independiente del JWT de autenticación.

    Se genera mediante secrets.token_urlsafe(), que utiliza
    una fuente criptográficamente segura de aleatoriedad.

    Este token puede utilizarse posteriormente para:

        1. Solicitar recuperación de contraseña.
        2. Enviar el token al correo del usuario.
        3. Validar el token.
        4. Permitir establecer una nueva contraseña.
    """

    return secrets.token_urlsafe(64)