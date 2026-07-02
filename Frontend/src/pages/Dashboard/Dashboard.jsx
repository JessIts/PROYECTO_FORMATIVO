import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Dashboard.module.css";
import ViewCoordinator from "./ViewCoordinator";
import ViewInstructor from "./ViewInstructor";
import ViewLearner from "./ViewLearner";
// IMPORTAMOS LOS ICONOS PROFESIONALES
import { LayoutDashboard, Calendar, Building2, Users, GraduationCap, BookOpen, FileText, Settings, Search, Bell, User, LogOut } from "lucide-react";

export default function Dashboard() {
  const [rol, setRol] = useState("coordinador");
  const navigate = useNavigate();

  return (
    <div className={styles.layout}>
      
{/* SIDEBAR */}
      <div className={styles.sidebar}>
        <div className={styles.logoContainer}>
          <img 
            src="https://upload.wikimedia.org/wikipedia/commons/8/83/Sena_Colombia_logo.svg" 
            alt="Logo SENA" 
            style={{ width: "70px", height: "70px", objectFit: "contain" }} 
          />
          <div style={{ display: "flex", flexDirection: "column", textAlign: "left", marginLeft: "8px" }}>
            <h2 style={{ margin: 0, fontSize: "20px", fontWeight: "700", color: "#0f172a" }}>SENA</h2>
            <span style={{ fontSize: "15px", color: "#64748b" }}>Gestión de Horarios</span>
          </div>
        </div>

        {/* Menú de opciones */}
        <div style={{ flex: 1, padding: "0 12px", display: "flex", flexDirection: "column", gap: "4px", marginTop: "10px" }}>
          <div className={styles.navItemActive}>
            <LayoutDashboard size={20} /> Dashboard
          </div>
          <div className={styles.navItem}><Calendar size={20} /> Horarios</div>
          <div className={styles.navItem}><Building2 size={20} /> Ambientes</div>
          <div className={styles.navItem}><Users size={20} /> Instructores</div>
          <div className={styles.navItem}><GraduationCap size={20} /> Aprendices</div>
          <div className={styles.navItem}><BookOpen size={20} /> Programas</div>
          <div className={styles.navItem}><FileText size={20} /> Reportes</div>
          <div className={styles.navItem}><Settings size={20} /> Configuración</div>
        </div>

        {/* 🚪 BOTÓN CERRAR SESIÓN (Fijado abajo del sidebar) */}
        <div className={styles.logoutContainer} onClick={() => navigate("/")}>
          <div className={styles.logoutItem}>
            <LogOut size={20} />
            <span>Cerrar Sesión</span>
          </div>
        </div>
      </div>
      {/* CONTENIDO PRINCIPAL */}
      <div className={styles.mainWrapper}>
        
        {/* HEADER */}
        <div className={styles.header}>
          <div className={styles.searchBox}>
            <Search size={18} style={{ color: "#94a3b8", marginRight: "10px" }} />
            <input 
              type="text" 
              placeholder="Buscar fichas, instructores, ambientes..." 
              className={styles.searchInput}
            />
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
            <Bell size={20} style={{ color: "#64748b", cursor: "pointer" }} />
            <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
              {/* Avatar con tus iniciales y el verde sena suave */}
              <div style={{ width: "38px", height: "38px", backgroundColor: "#dcfce7", color: "#16a34a", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "14px", fontWeight: "700" }}>
                DM
              </div>
              <span style={{ fontSize: "14px", fontWeight: "600", color: "#0f172a" }}>Administrador</span>
            </div>
          </div>
        </div>
        {/* ÁREA DINÁMICA */}
        <div className={styles.contentArea}>
          {rol === "coordinador" && <ViewCoordinator />}
          {rol === "instructor" && <ViewInstructor />}
          {rol === "aprendiz" && <ViewLearner />}
        </div>

      </div>
    </div>
  );
}