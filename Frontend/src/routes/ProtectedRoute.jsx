import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function ProtectedRoute({ children }) {

    const {
        isAuthenticated,
        loading,
        user
    } = useAuth();

    // Mientras verificamos la autenticación
    if (loading) {
        return <div>Cargando...</div>;
    }

    // Usuario no autenticado
    if (!isAuthenticated) {
        return <Navigate to="/" replace />;
    }

    // Roles del usuario
    const roles = user?.roles || [];

    // Roles permitidos
    const rolesValidos = [
        "COORDINADOR",
        "INSTRUCTOR",
        "APRENDIZ"
    ];

    // Verificar si tiene al menos un rol válido
    const tieneRolValido = roles.some(
        (rol) =>
            rolesValidos.includes(
                rol?.nombre?.toUpperCase()
            )
    );

    // Usuario autenticado pero sin permisos
    if (!tieneRolValido) {
        return <Navigate to="/acceso-denegado" replace />;
    }

    // Usuario autorizado
    return children;
}