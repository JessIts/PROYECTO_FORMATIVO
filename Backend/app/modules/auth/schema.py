from pydantic import BaseModel
from pydantic import EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

#token para el login
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ForgotPasswordRequest(BaseModel):
    email: str

class ResetPasswordRequest(BaseModel):
    token: str
    nueva_password: str