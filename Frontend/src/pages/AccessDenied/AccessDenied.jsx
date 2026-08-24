import { useNavigate } from "react-router-dom";
import { ShieldX, LogOut } from "lucide-react";
import styles from "./AccessDenied.module.css";
import { useAuth } from "../../context/AuthContext";

export default function AccessDenied() {

    const navigate = useNavigate();
    const { logout } = useAuth();

    const handleLogout = () => {
        logout();
    };

    return (
        <div className={styles.container}>

            <div className={styles.card}>

                <div className={styles.iconContainer}>
                    <ShieldX size={48} />
                </div>

                <h1>Acceso denegado</h1>

                <p className={styles.title}>
                    No tienes permisos para acceder al sistema.
                </p>

                <p className={styles.description}>
                    Tu usuario está autenticado, pero no tiene
                    un rol asignado que permita acceder al dashboard.
                </p>

                <div className={styles.actions}>

                    <button
                        className={styles.primaryButton}
                        onClick={handleLogout}
                    >
                        <LogOut size={18} />
                        Cerrar sesión
                    </button>

                </div>

            </div>

        </div>
    );
}