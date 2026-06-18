from app.modules.auth.password_token_model import (
    PasswordResetToken
)


class AuthRepository:

    @staticmethod
    def guardar_token(
        db,
        token_obj
    ):
        db.add(token_obj)
        db.commit()
        db.refresh(token_obj)

        return token_obj

    @staticmethod
    def obtener_token(
        db,
        token
    ):
        return (
            db.query(
                PasswordResetToken
            )
            .filter(
                PasswordResetToken.token == token
            )
            .first()
        )