from fastapi import HTTPException

from .service import AuthService

class AuthController:

    @staticmethod
    def login(
        db,
        data
    ):
        try:

            return AuthService.login(
                db,
                data.email,
                data.password
            )

        except Exception as e:

            raise HTTPException(
                status_code=401,
                detail=str(e)
            )