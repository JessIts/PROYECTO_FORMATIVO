import { useState } from "react";

import "./../auth.css";

import { useAuth } from "../context/AuthContext";

import {
  useNavigate,
  Link
} from "react-router-dom";


export default function Login() {

  const navigate = useNavigate();

  const { login } = useAuth();


  const [form, setForm] = useState({
    correoElectronico: "",
    password: "",
  });


  const [error, setError] = useState("");

  const [loading, setLoading] = useState(false);


  // ============================================================
  // CAMBIAR INPUT
  // ============================================================

  const handleChange = (e) => {

    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });

  };


  // ============================================================
  // LOGIN
  // ============================================================

  const handleSubmit = async (e) => {

  e.preventDefault();

  setError("");

  if (!form.correoElectronico || !form.password) {

    setError(
      "Debes ingresar tu correo electrónico y contraseña."
    );

    return;
  }


  try {

    setLoading(true);


    await login(form);


    setForm({
      correoElectronico: "",
      password: ""
    });


    navigate("/dashboard");


  } catch (error) {

    console.error(
      "Error en login:",
      error
    );


    setError(
      error.message ||
      "No se pudo conectar con el servidor."
    );


  } finally {

    setLoading(false);

  }

};


  return (

    <div className="container">

      <div className="card login-card">


        <div className="icon-box">
          🔐
        </div>


        <h2>
          Bienvenido
        </h2>


        <p className="subtitle">
          Ingresa tus credenciales para acceder a tu cuenta
        </p>


        <form onSubmit={handleSubmit}>


          <label>
            Correo electrónico
          </label>


          <input
            type="email"
            name="correoElectronico"
            placeholder="ej: usuario@email.com"
            value={form.correoElectronico}
            onChange={handleChange}
          />


          <label>
            Contraseña
          </label>


          <input
            type="password"
            name="password"
            placeholder="********"
            value={form.password}
            onChange={handleChange}
          />


          {error && (

            <p className="error-message">
              {error}
            </p>

          )}


          <div className="row">

            <label className="remember">

              <input type="checkbox" />

              Recordarme

            </label>


            <Link
              to="/forgot-password"
              className="link"
            >
              ¿Olvidaste tu contraseña?
            </Link>

          </div>


          <button
            type="submit"
            disabled={loading}
          >

            {loading
              ? "Iniciando sesión..."
              : "Iniciar sesión"
            }

          </button>


        </form>


        <p className="bottom-text">

          ¿No tienes cuenta?{" "}

          <Link to="/register-role">
            Regístrate
          </Link>

        </p>


      </div>

    </div>

  );
}