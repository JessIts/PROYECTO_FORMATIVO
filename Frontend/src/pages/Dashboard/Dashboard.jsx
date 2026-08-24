import React from "react";

import styles from "./Dashboard.module.css";

import ViewCoordinator from "./ViewCoordinator";
import ViewInstructor from "./ViewInstructor";
import ViewLearner from "./ViewLearner";

import { useAuth } from "../../context/AuthContext";

import {
    LayoutDashboard,
    Calendar,
    Building2,
    Users,
    GraduationCap,
    BookOpen,
    FileText,
    Settings,
    Search,
    Bell,
    LogOut
} from "lucide-react";


export default function Dashboard() {

    const {
        user,
        logout
    } = useAuth();


    // ============================================================
    // OBTENER NOMBRE COMPLETO
    // ============================================================

    const nombreCompleto = [
        user?.nombres,
        user?.apellidos
    ]
        .filter(Boolean)
        .join(" ");


    // ============================================================
    // OBTENER INICIALES
    // ============================================================

    const iniciales = [
        user?.nombres?.charAt(0),
        user?.apellidos?.charAt(0)
    ]
        .filter(Boolean)
        .join("")
        .toUpperCase();


    // ============================================================
    // OBTENER ROLES
    // ============================================================

    const roles = user?.roles || [];


    // ============================================================
    // IDENTIFICAR ROL DEL USUARIO
    // ============================================================

    const tieneRol = (nombreRol) => {
        return roles.some(
            (rol) =>
                rol?.nombre?.toUpperCase() === nombreRol
        );
    };


    const esCoordinador = tieneRol("COORDINADOR");

    const esInstructor = tieneRol("INSTRUCTOR");

    const esAprendiz = tieneRol("APRENDIZ");


    // ============================================================
    // OBTENER NOMBRE DEL ROL
    // ============================================================

    const nombreRol =
        roles.length > 0
            ? roles
                .map((rol) => rol?.nombre)
                .filter(Boolean)
                .join(", ")
            : "Sin rol";


    // ============================================================
    // LOGOUT
    // ============================================================

    const handleLogout = () => {
        logout();
    };


    // ============================================================
    // VISTA SEGÚN ROL
    // ============================================================

    const renderRoleView = () => {

        if (esCoordinador) {
            return <ViewCoordinator />;
        }

        if (esInstructor) {
            return <ViewInstructor />;
        }

        if (esAprendiz) {
            return <ViewLearner />;
        }

        return (
            <div>
                <h2>Acceso no disponible</h2>

                <p>
                    El usuario no tiene un rol válido
                    para acceder al dashboard.
                </p>
            </div>
        );
    };


    return (
        <div className={styles.layout}>

            {/* ======================================================
                SIDEBAR
            ====================================================== */}

            <div className={styles.sidebar}>

                {/* LOGO */}

                <div className={styles.logoContainer}>

                    <img
                        src="https://upload.wikimedia.org/wikipedia/commons/8/83/Sena_Colombia_logo.svg"
                        alt="Logo SENA"
                        style={{
                            width: "70px",
                            height: "70px",
                            objectFit: "contain"
                        }}
                    />

                    <div
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            textAlign: "left",
                            marginLeft: "8px"
                        }}
                    >

                        <h2
                            style={{
                                margin: 0,
                                fontSize: "20px",
                                fontWeight: "700",
                                color: "#0f172a"
                            }}
                        >
                            SENA
                        </h2>

                        <span
                            style={{
                                fontSize: "15px",
                                color: "#64748b"
                            }}
                        >
                            Gestión de Horarios
                        </span>

                    </div>

                </div>


                {/* MENÚ */}

                <div
                    style={{
                        flex: 1,
                        padding: "0 12px",
                        display: "flex",
                        flexDirection: "column",
                        gap: "4px",
                        marginTop: "10px"
                    }}
                >

                    <div className={styles.navItemActive}>
                        <LayoutDashboard size={20} />
                        Dashboard
                    </div>


                    <div className={styles.navItem}>
                        <Calendar size={20} />
                        Horarios
                    </div>


                    <div className={styles.navItem}>
                        <Building2 size={20} />
                        Ambientes
                    </div>


                    <div className={styles.navItem}>
                        <Users size={20} />
                        Instructores
                    </div>


                    <div className={styles.navItem}>
                        <GraduationCap size={20} />
                        Aprendices
                    </div>


                    <div className={styles.navItem}>
                        <BookOpen size={20} />
                        Programas
                    </div>


                    <div className={styles.navItem}>
                        <FileText size={20} />
                        Reportes
                    </div>


                    <div className={styles.navItem}>
                        <Settings size={20} />
                        Configuración
                    </div>

                </div>


                {/* ====================================================
                    CERRAR SESIÓN
                ==================================================== */}

                <div
                    className={styles.logoutContainer}
                    onClick={handleLogout}
                >

                    <div className={styles.logoutItem}>

                        <LogOut size={20} />

                        <span>
                            Cerrar Sesión
                        </span>

                    </div>

                </div>

            </div>


            {/* ======================================================
                CONTENIDO PRINCIPAL
            ====================================================== */}

            <div className={styles.mainWrapper}>


                {/* HEADER */}

                <div className={styles.header}>


                    {/* BUSCADOR */}

                    <div className={styles.searchBox}>

                        <Search
                            size={18}
                            style={{
                                color: "#94a3b8",
                                marginRight: "10px"
                            }}
                        />

                        <input
                            type="text"
                            placeholder="Buscar fichas, instructores, ambientes..."
                            className={styles.searchInput}
                        />

                    </div>


                    {/* USUARIO */}

                    <div
                        style={{
                            display: "flex",
                            alignItems: "center",
                            gap: "20px"
                        }}
                    >

                        <Bell
                            size={20}
                            style={{
                                color: "#64748b",
                                cursor: "pointer"
                            }}
                        />


                        <div
                            style={{
                                display: "flex",
                                alignItems: "center",
                                gap: "12px"
                            }}
                        >

                            {/* AVATAR */}

                            <div
                                style={{
                                    width: "38px",
                                    height: "38px",
                                    backgroundColor: "#dcfce7",
                                    color: "#16a34a",
                                    borderRadius: "50%",
                                    display: "flex",
                                    alignItems: "center",
                                    justifyContent: "center",
                                    fontSize: "14px",
                                    fontWeight: "700"
                                }}
                            >
                                {iniciales || "U"}
                            </div>


                            {/* NOMBRE */}

                            <div
                                style={{
                                    display: "flex",
                                    flexDirection: "column"
                                }}
                            >

                                <span
                                    style={{
                                        fontSize: "14px",
                                        fontWeight: "600",
                                        color: "#0f172a"
                                    }}
                                >
                                    {nombreCompleto || "Usuario"}
                                </span>

                                <span
                                    style={{
                                        fontSize: "12px",
                                        color: "#64748b"
                                    }}
                                >
                                    {nombreRol}
                                </span>

                            </div>

                        </div>

                    </div>

                </div>


                {/* ====================================================
                    ÁREA DINÁMICA
                ==================================================== */}

                <div className={styles.contentArea}>

                    {renderRoleView()}

                </div>

            </div>

        </div>
    );
}