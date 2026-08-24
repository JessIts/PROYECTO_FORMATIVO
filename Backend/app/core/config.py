from dotenv import load_dotenv
import os


load_dotenv()


# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)


# ============================================================
# JWT
# ============================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 5


# ============================================================
# FRONTEND
# ============================================================

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173"
)


# ============================================================
# BREVO
# ============================================================

BREVO_API_KEY = os.getenv(
    "BREVO_API_KEY"
)

MAIL_FROM = os.getenv(
    "MAIL_FROM"
)

MAIL_FROM_NAME = os.getenv(
    "MAIL_FROM_NAME",
    "SENA Gestión de Horarios"
)