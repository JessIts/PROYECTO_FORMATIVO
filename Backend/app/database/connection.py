# ============================================================
# app/database/connection.py
# ============================================================

# ------------------------------------------------------------
# SQLAlchemy
#
# create_engine:
#     Crea el motor de conexión con PostgreSQL.
#
# sessionmaker:
#     Crea las sesiones que utilizaremos para consultar
#     y modificar la base de datos.
# ------------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# ------------------------------------------------------------
# URL de conexión
#
# DATABASE_URL contiene los datos necesarios para conectarse
# a PostgreSQL.
# ------------------------------------------------------------

from app.core.config import DATABASE_URL


# ============================================================
# ENGINE
# ============================================================

# ------------------------------------------------------------
# Creamos el engine utilizando DATABASE_URL.
#
# Ejemplo de DATABASE_URL:
#
# postgresql://usuario:password@localhost:5432/sihs
#
# SQLAlchemy detectará el driver PostgreSQL especificado
# en la URL.
# ------------------------------------------------------------

engine = create_engine(
    DATABASE_URL
)


# ============================================================
# SESSION LOCAL
# ============================================================

# ------------------------------------------------------------
# sessionmaker crea las sesiones que utilizará nuestra
# aplicación para comunicarse con PostgreSQL.
#
# autocommit=False:
#     Los cambios no se confirman automáticamente.
#
# autoflush=False:
#     SQLAlchemy no enviará automáticamente los cambios
#     pendientes antes de cada consulta.
#
# bind=engine:
#     Vincula las sesiones con nuestro engine.
# ------------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ============================================================
# DEPENDENCIA DE BASE DE DATOS
# ============================================================

def get_db():
    """
    Crea una sesión de base de datos para una petición.

    FastAPI utilizará esta función mediante Depends():

        db: Session = Depends(get_db)

    Cuando termina la petición, la sesión se cierra
    automáticamente.
    """

    # --------------------------------------------------------
    # Creamos una nueva sesión.
    # --------------------------------------------------------

    db = SessionLocal()

    try:

        # ----------------------------------------------------
        # Entregamos la sesión al endpoint, service o
        # repository que la necesite.
        # ----------------------------------------------------

        yield db

    finally:

        # ----------------------------------------------------
        # Cerramos siempre la conexión/sesión.
        #
        # Esto evita dejar conexiones abiertas en PostgreSQL.
        # ----------------------------------------------------

        db.close()