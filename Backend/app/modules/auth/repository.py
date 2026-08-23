from sqlalchemy.orm import Session

from app.modules.auth.password_token_model import PasswordResetToken


class AuthRepository:

    @staticmethod
    def guardar_token(
        db: Session,
        token_obj: PasswordResetToken
    ) -> PasswordResetToken:

        db.add(token_obj)
        db.commit()
        db.refresh(token_obj)

        return token_obj

    @staticmethod
    def obtener_token(
        db: Session,
        token: str
    ) -> PasswordResetToken | None:

        return (
            db.query(PasswordResetToken)
            .filter(
                PasswordResetToken.token == token
            )
            .first()
        )

    @staticmethod
    def actualizar_token(
        db: Session,
        token_obj: PasswordResetToken
    ) -> PasswordResetToken:

        db.commit()
        db.refresh(token_obj)

        return token_obj

    @staticmethod
    def eliminar_token(
        db: Session,
        token_obj: PasswordResetToken
    ) -> None:

        db.delete(token_obj)
        db.commit()