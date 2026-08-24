import { useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";

import "./../auth.css";

import { resetPasswordRequest } from "../api/auth.api";

export default function ResetPassword() {

    const navigate = useNavigate();

    const [searchParams] = useSearchParams();

    const token = searchParams.get("token");

    const [newPassword, setNewPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        setMessage("");

        if (!token) {

            setMessage(
                "El enlace de recuperación no es válido."
            );

            return;
        }

        if (newPassword !== confirmPassword) {

            setMessage(
                "Las contraseñas no coinciden."
            );

            return;
        }

        if (newPassword.length < 8) {

            setMessage(
                "La contraseña debe tener al menos 8 caracteres."
            );

            return;
        }

        try {

            setLoading(true);

            const res = await resetPasswordRequest({
                token: token,
                nuevaPassword: newPassword
            });

            if (res.success || res.message) {

                alert(
                    "Contraseña actualizada correctamente."
                );

                navigate("/");

            } else {

                setMessage(
                    res.message ||
                    "No fue posible actualizar la contraseña."
                );
            }

        } catch (error) {

            console.error(error);

            setMessage(
                "El enlace no es válido o ha expirado."
            );

        } finally {

            setLoading(false);

        }
    };

    return (
        <div className="container">

            <div className="card">

                <h2>
                    Nueva contraseña
                </h2>

                {!token ? (

                    <p>
                        El enlace de recuperación no es válido.
                    </p>

                ) : (

                    <form onSubmit={handleSubmit}>

                        <input
                            type="password"
                            placeholder="Nueva contraseña"
                            value={newPassword}
                            onChange={(e) =>
                                setNewPassword(e.target.value)
                            }
                            required
                        />

                        <input
                            type="password"
                            placeholder="Confirmar contraseña"
                            value={confirmPassword}
                            onChange={(e) =>
                                setConfirmPassword(e.target.value)
                            }
                            required
                        />

                        <button
                            type="submit"
                            disabled={loading}
                        >
                            {loading
                                ? "Actualizando..."
                                : "Actualizar contraseña"
                            }
                        </button>

                    </form>

                )}

                {message && (
                    <p>
                        {message}
                    </p>
                )}

            </div>

        </div>
    );
}