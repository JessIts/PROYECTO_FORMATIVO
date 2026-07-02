import { useState } from "react";
import "./../auth.css";
import { forgotPasswordRequest, resetPasswordRequest } from "../api/auth.api";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const [newPassword, setNewPassword] = useState("");

  const [showCodeModal, setShowCodeModal] = useState(false);
  const [showPasswordModal, setShowPasswordModal] = useState(false);

  // enviar correo
  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await forgotPasswordRequest({ email });

    if (res.success || res.message) {
      setShowCodeModal(true);
    } else {
      alert("Error enviando código");
    }
  };

  // validar código 
  const handleVerifyCode = () => {
    setShowCodeModal(false);
    setShowPasswordModal(true);
  };

  // cambiar password
  const handleResetPassword = async () => {
    const res = await resetPasswordRequest({
      email,
      code,
      password: newPassword,
    });

    if (res.success || res.message) {
      alert("Contraseña actualizada");
      window.location.href = "/";
    } else {
      alert("Error");
    }
  };

  return (
    <div className="fp-container">

      {/* CARD PRINCIPAL */}
      <div className="fp-card">

        <div className="fp-icon">✉️</div>

        <h2>Recuperar Contraseña</h2>

        <p>Ingresa tu correo y te enviaremos instrucciones</p>

        <form onSubmit={handleSubmit}>
          <label>Correo electrónico</label>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="tucorreo@gmail.com"
          />

          <button type="submit">
            Enviar instrucciones
          </button>
        </form>

        <a href="/" className="fp-back">
          ← Volver al inicio de sesión
        </a>

      </div>

      {/*  MODAL 1 - CÓDIGO */}
      {showCodeModal && (
        <div className="modal-overlay">
          <div className="modal-card">
            <h3>Ingresa el código</h3>

            <input
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="Código"
            />

            <button onClick={handleVerifyCode}>
              Verificar
            </button>
          </div>
        </div>
      )}

      {/* MODAL 2 - PASSWORD */}
      {showPasswordModal && (
        <div className="modal-overlay">
          <div className="modal-card">
            <h3>Nueva contraseña</h3>

            <input
              type="password"
              placeholder="Nueva contraseña"
              onChange={(e) => setNewPassword(e.target.value)}
            />

            <button onClick={handleResetPassword}>
              Guardar
            </button>
          </div>
        </div>
      )}

    </div>
  );
}