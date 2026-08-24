import { useState } from "react";
import { useNavigate } from "react-router-dom";

import "./../auth.css";

import { forgotPasswordRequest } from "../api/auth.api";

export default function ForgotPassword() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        if (!email.trim()) {
            setMessage("Ingresa tu correo electrónico.");
            return;
        }

        try {

            setLoading(true);
            setMessage("");

            const res = await forgotPasswordRequest({
                correoElectronico: email
            });

            if (res.success || res.message) {

                setMessage(
                    "Si el correo está registrado, recibirás un enlace para restablecer tu contraseña."
                );

                setEmail("");

            } else {

                setMessage(
                    res.message ||
                    "No fue posible procesar la solicitud."
                );
            }

        } catch (error) {

            console.error(error);

            setMessage(
                "No fue posible conectar con el servidor."
            );

        } finally {

            setLoading(false);

        }
    };

    return (
        <div className="fp-container">

            <div className="fp-card">

                <div className="fp-icon">
                    ✉️
                </div>

                <h2>
                    Recuperar Contraseña
                </h2>

                <p>
                    Ingresa tu correo electrónico y
                    te enviaremos un enlace para
                    restablecer tu contraseña.
                </p>

                <form onSubmit={handleSubmit}>

                    <label>
                        Correo electrónico
                    </label>

                    <input
                        type="email"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                        placeholder="tucorreo@gmail.com"
                        required
                    />

                    <button
                        type="submit"
                        disabled={loading}
                    >
                        {loading
                            ? "Enviando..."
                            : "Enviar instrucciones"
                        }
                    </button>

                </form>

                {message && (
                    <p>
                        {message}
                    </p>
                )}

                <button
                    type="button"
                    className="fp-back"
                    onClick={() => navigate("/")}
                >
                    ← Volver al inicio de sesión
                </button>

            </div>

        </div>
    );
}