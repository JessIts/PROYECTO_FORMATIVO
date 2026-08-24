import requests

from app.core.config import (
    BREVO_API_KEY,
    MAIL_FROM,
    MAIL_FROM_NAME
)


print("BREVO_API_KEY CARGADA:", bool(BREVO_API_KEY))
print("LONGITUD API KEY:", len(BREVO_API_KEY) if BREVO_API_KEY else 0)
print("MAIL_FROM:", MAIL_FROM)

def enviar_correo_recuperacion(
    correo_destino: str,
    enlace: str
):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": MAIL_FROM_NAME,
            "email": MAIL_FROM
        },
        "to": [
            {
                "email": correo_destino
            }
        ],
        "subject": "Restablecimiento de contraseña",
        "htmlContent": f"""
            <html>
                <body>
                    <h2>Restablecimiento de contraseña</h2>

                    <p>
                        Has solicitado restablecer tu contraseña.
                    </p>

                    <p>
                        Haz clic en el siguiente botón:
                    </p>

                    <p>
                        <a href="{enlace}">
                            Restablecer contraseña
                        </a>
                    </p>

                    <p>
                        Este enlace será válido durante 30 minutos.
                    </p>

                    <p>
                        Si no solicitaste este cambio,
                        puedes ignorar este correo.
                    </p>
                </body>
            </html>
        """
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )

    if not response.ok:
        raise Exception(
            f"Error enviando correo: {response.text}"
        )

    return response.json()

def probar_brevo():

    url = "https://api.brevo.com/v3/account"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print("================================")
    print("BREVO TEST")
    print("STATUS:", response.status_code)
    print("RESPUESTA:", response.text)
    print("================================")

    return response