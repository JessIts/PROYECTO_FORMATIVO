import { useState } from "react";
import "./../auth.css";
import { resetPasswordRequest } from "../api/auth.api";

export default function ResetPassword() {
  const [form, setForm] = useState({
    email: "",
    code: "",
    new_password: "",
    confirm_password: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (form.new_password !== form.confirm_password) {
      alert("Las contraseñas no coinciden");
      return;
    }

    try {
      const res = await resetPasswordRequest({
        email: form.email,
        token: form.code, 
        new_password: form.new_password,
      });

      if (res.success || res.message) {
        alert("Contraseña actualizada");
        window.location.href = "/";
      } else {
        alert(res.message || "Error al actualizar contraseña");
      }
    } catch (error) {
      console.error(error);
      alert("Error de conexión con el servidor");
    }
  };

  return (
    <div className="container">
      <div className="card">

        <h2>Nueva contraseña</h2>

        <form onSubmit={handleSubmit}>

          <input
            name="email"
            placeholder="Correo"
            onChange={handleChange}
          />

          <input
            name="code"
            placeholder="Código"
            onChange={handleChange}
          />

          <input
            name="new_password"
            type="password"
            placeholder="Nueva contraseña"
            onChange={handleChange}
          />

          <input
            name="confirm_password"
            type="password"
            placeholder="Confirmar contraseña"
            onChange={handleChange}
          />

          <button type="submit">
            Actualizar
          </button>

        </form>

      </div>
    </div>
  );
}