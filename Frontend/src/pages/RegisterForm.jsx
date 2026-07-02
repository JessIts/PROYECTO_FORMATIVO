import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import { registerRequest } from "../api/auth.api";

export default function RegisterForm() {
  const { state } = useLocation();
  const navigate = useNavigate();
  const role = state?.role;

  const [form, setForm] = useState({
    nombres: "",
    apellidos: "",
    numero_documento: "",
    tipo_documento: "",
    correo: "",
    telefono: "",
    codigo: "",
    especialidad: "",
    ficha: "",
    programa: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const validateRole = () => {
    if (!role) {
      alert("Debe seleccionar un rol");
      return false;
    }

    if (!form.nombres || !form.apellidos || !form.numero_documento) {
      alert("Complete los campos obligatorios");
      return false;
    }

    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateRole()) return;

    const payload = {
      rol: role,
      nombres: form.nombres,
      apellidos: form.apellidos,
      numero_documento: form.numero_documento,
      tipo_documento: form.tipo_documento,
      correo: form.correo,
      telefono: form.telefono,

      ...(role === "instructor" && {
        codigo_instructor: form.codigo,
        especialidad: form.especialidad
      }),

      ...(role === "aprendiz" && {
        codigo_ficha: form.ficha,
        programa_formacion: form.programa
      })
    };

    try {
      const res = await registerRequest(payload);

      if (res.message || res.success || res.id) {
        alert("Registro exitoso");

        navigate("/set-password", {
          state: { email: form.correo }
        });
      } else {
        alert(res.message || "Error en registro");
      }
    } catch (error) {
      console.error(error);
      alert("Error de conexión con el servidor");
    }
  };

  return (
    <div className="container">
      <div className="card">

        <h2>Registro de Usuario</h2>
        <h4>Rol: {role}</h4>

        <form onSubmit={handleSubmit}>

          <input
            name="nombres"
            placeholder="Nombres"
            onChange={handleChange}
          />

          <input
            name="apellidos"
            placeholder="Apellidos"
            onChange={handleChange}
          />

          <input
            name="numero_documento"
            placeholder="Número de documento"
            onChange={handleChange}
          />

          {}
          <select
            name="tipo_documento"
            value={form.tipo_documento}
            onChange={handleChange}
          >
            <option value="">Seleccione tipo de documento</option>
            <option value="CC">Cédula de ciudadanía</option>
            <option value="TI">Tarjeta de identidad</option>
            <option value="CE">Cédula de extranjería</option>
            <option value="PP">Pasaporte</option>
          </select>

          <input
            name="correo"
            placeholder="Correo electrónico"
            onChange={handleChange}
          />

          <input
            name="telefono"
            placeholder="Teléfono"
            onChange={handleChange}
          />

          {/*  CAMPOS INSTRUCTOR */}
          {role === "instructor" && (
            <>
              <input
                name="codigo"
                placeholder="Código instructor"
                onChange={handleChange}
              />

              <input
                name="especialidad"
                placeholder="Especialidad"
                onChange={handleChange}
              />
            </>
          )}

          {/*  CAMPOS APRENDIZ */}
          {role === "aprendiz" && (
            <>
              <input
                name="ficha"
                placeholder="Código de ficha"
                onChange={handleChange}
              />

              <input
                name="programa"
                placeholder="Programa de formación"
                onChange={handleChange}
              />
            </>
          )}

          {/*  COORDINADOR */}
          {role === "coordinador" && (
            <p>
              ⚠ Registro sujeto a aprobación del administrador
            </p>
          )}

          <button type="submit">
            Registrar
          </button>

        </form>
      </div>
    </div>
  );
}