import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function RegisterRole() {
  const [role, setRole] = useState("");
  const navigate = useNavigate();

  const next = () => {
    if (!role) return alert("Selecciona un rol");

    navigate("/register-form", { state: { role } });
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Registro</h2>

        <select onChange={(e) => setRole(e.target.value)}>
          <option value="">Seleccione rol</option>
          <option value="coordinador">Coordinador</option>
          <option value="instructor">Instructor</option>
          <option value="aprendiz">Aprendiz</option>
        </select>

        <button onClick={next}>Continuar</button>
      </div>
    </div>
  );
}