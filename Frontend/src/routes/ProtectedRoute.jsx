import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";

import { getCurrentUserRequest } from "../api/auth.api";

export default function ProtectedRoute({ children }) {

  const [loading, setLoading] = useState(true);
  const [authenticated, setAuthenticated] = useState(false);

  useEffect(() => {

    const validateSession = async () => {

      const token = localStorage.getItem("token");

      if (!token) {
        setAuthenticated(false);
        setLoading(false);
        return;
      }

      try {

        await getCurrentUserRequest();

        setAuthenticated(true);

      } catch (error) {

        console.error(
          "Sesión inválida:",
          error
        );

        localStorage.removeItem("token");

        setAuthenticated(false);

      } finally {

        setLoading(false);

      }
    };

    validateSession();

  }, []);

  if (loading) {
    return <div>Verificando sesión...</div>;
  }

  if (!authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}