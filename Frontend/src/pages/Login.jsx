import { useState } from "react";
import "./../auth.css";
import { loginRequest } from "../api/auth.api";
import { useNavigate, Link } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    document: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await loginRequest(form);

    if (res.access_token) {
      localStorage.setItem("token", res.access_token);

      setForm({ document: "", password: "" });

      navigate("/home");
    } else {
      alert("Error en login");
    }
  };

  return (
    <div className="container">
      <div className="card login-card">

        {/* ICONO */}
        <div className="icon-box">
          🔐
        </div>

        <h2>Bienvenido</h2>
        <p className="subtitle">
          Ingresa tus credenciales para acceder a tu cuenta
        </p>

        <form onSubmit={handleSubmit}>

          <label>Correo electrónico</label>
          <input
            name="document"
            placeholder="ej: usuario@email.com"
            onChange={handleChange}
          />

          <label>Contraseña</label>
          <input
            type="password"
            name="password"
            placeholder="********"
            onChange={handleChange}
          />

          <div className="row">
            <label className="remember">
              <input type="checkbox" /> Recordarme
            </label>

            <Link to="/forgot-password" className="link">
              ¿Olvidaste tu contraseña?
            </Link>
          </div>

          <button type="submit">Iniciar sesión</button>

        </form>

        <p className="bottom-text">
          ¿No tienes cuenta?{" "}
          <Link to="/register-role">Regístrate</Link>
        </p>

      </div>
    </div>
  );
}