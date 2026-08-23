# ============================================================
# app/modules/auth/schema.py
# ============================================================

from pydantic import BaseModel, EmailStr


# ============================================================
# LOGIN
# ============================================================

class LoginRequest(BaseModel):
    """
    Credenciales utilizadas para iniciar sesión.
    """

    correoElectronico: EmailStr
    password: str


# ============================================================
# RESPUESTA JWT
# ============================================================

class TokenResponse(BaseModel):
    """
    Respuesta generada después de un login exitoso.
    """

    access_token: str
    token_type: str = "bearer"


# ============================================================
# CAMBIAR CONTRASEÑA
# ============================================================

class CambiarPasswordRequest(BaseModel):
    """
    Datos necesarios para cambiar la contraseña
    de un usuario autenticado.
    """

    passwordActual: str
    nuevaPassword: str


# ============================================================
# SOLICITAR RECUPERACIÓN DE CONTRASEÑA
# ============================================================

class ForgotPasswordRequest(BaseModel):
    """
    Solicitud para iniciar la recuperación
    de contraseña.

    El usuario proporciona su correo electrónico.
    """

    correoElectronico: EmailStr


# ============================================================
# RESTABLECER CONTRASEÑA
# ============================================================

class ResetPasswordRequest(BaseModel):
    """
    Datos necesarios para restablecer la contraseña
    utilizando un token de recuperación.
    """

    token: str
    nuevaPassword: str