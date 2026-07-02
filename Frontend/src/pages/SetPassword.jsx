import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { setPasswordRequest } from "../api/auth.api";

export default function SetPassword() {
  const { state } = useLocation();
  const navigate = useNavigate();

  const email = state?.email;

  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");

  const validate = (p) =>
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/.test(p);

  const handleSubmit = async () => {
    if (!email) {
      alert("No hay email, vuelve a registrarte");
      return navigate("/register-role");
    }

    if (password !== confirm) {
      return alert("Las contraseñas no coinciden");
    }

    if (!validate(password)) {
      return alert("La contraseña no cumple los requisitos de seguridad");
    }

    try {
      const res = await setPasswordRequest({
        email,
        new_password: password, // 
      });

      if (res.success || res.message) {
        alert("Registro completado");
        navigate("/");
      } else {
        alert(res.message || "Error al crear contraseña");
      }
    } catch (error) {
      console.error(error);
      alert("Error de conexión con el servidor");
    }
  };

  return (
    <div className="container">
      <div className="card">

        <h2>Crear contraseña</h2>

        <input
          type="password"
          placeholder="Contraseña"
          onChange={(e) => setPassword(e.target.value)}
        />

        <input
          type="password"
          placeholder="Confirmar contraseña"
          onChange={(e) => setConfirm(e.target.value)}
        />

        <button onClick={handleSubmit}>
          Guardar
        </button>

      </div>
    </div>
  );
}