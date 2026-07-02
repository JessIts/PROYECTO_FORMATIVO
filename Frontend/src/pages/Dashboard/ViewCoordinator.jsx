import React from "react";
import styles from "./Dashboard.module.css";
// Importamos los iconos exactos con la iconografía estilizada de la referencia
import { Building2, UserCheck, GraduationCap, Calendar, Clock, ChevronRight, CalendarCheck} from "lucide-react";

export default function ViewCoordinator() {
  
  const fechaActual = new Date().toLocaleDateString('es-CO', { 
    weekday: 'long', 
    day: 'numeric', 
    month: 'long', 
    year: 'numeric' 
  });

  return (
    <div style={{ color: "#1e293b", width: "100%", maxWidth: "1200px", margin: "0 auto" }}>
      
      {/* 1. BIENVENIDA */}
      <div style={{ marginBottom: "30px", textAlign: "left" }}>
        <h1 style={{ fontSize: "28px", fontWeight: "700", color: "#0f172a", margin: "0 0 5px 0" }}>
          Bienvenido al Sistema de Horarios 📚
        </h1>
        <p style={{ color: "#475569", margin: 0, fontSize: "15px", fontWeight: "500" }}>
          Centro de Formación - {fechaActual}
        </p>
      </div>

      {/* 2. TARJETAS SUPERIORES (Con el estilo e iconos estilizados de la referencia) */}
      <div className={styles.gridTop}>
        
        {/* Total Ambientes */}
        <div className={styles.statCard}>
          <div style={{ width: "42px", height: "42px", borderRadius: "10px", backgroundColor: "#2563eb", color: "white", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: "15px" }}>
            <Building2 size={22} strokeWidth={1.8} />
          </div>
          <p style={{ color: "#64748b", fontSize: "14px", fontWeight: "500", margin: "0 0 5px 0" }}>Total Ambientes</p>
          <div style={{ fontSize: "28px", fontWeight: "700", color: "#0f172a", margin: "0 0 5px 0" }}>45</div>
          <span style={{ color: "#94a3b8", fontSize: "12px", fontWeight: "500" }}>5 en mantenimiento</span>
        </div>
        
        {/* Instructores Activos */}
        <div className={styles.statCard}>
          <div style={{ width: "42px", height: "42px", borderRadius: "10px", backgroundColor: "#16a34a", color: "white", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: "15px" }}>
            <UserCheck size={22} strokeWidth={1.8} />
          </div>
          <p style={{ color: "#64748b", fontSize: "14px", fontWeight: "500", margin: "0 0 5px 0" }}>Instructores Activos</p>
          <div style={{ fontSize: "28px", fontWeight: "700", color: "#0f172a", margin: "0 0 5px 0" }}>128</div>
          <span style={{ color: "#94a3b8", fontSize: "12px", fontWeight: "500" }}>15 nuevos este mes</span>
        </div>

        {/* Aprendices */}
        <div className={styles.statCard}>
          <div style={{ width: "42px", height: "42px", borderRadius: "10px", backgroundColor: "#9333ea", color: "white", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: "15px" }}>
            <GraduationCap size={22} strokeWidth={1.8} />
          </div>
          <p style={{ color: "#64748b", fontSize: "14px", fontWeight: "500", margin: "0 0 5px 0" }}>Aprendices</p>
          <div style={{ fontSize: "28px", fontWeight: "700", color: "#0f172a", margin: "0 0 5px 0" }}>2,456</div>
          <span style={{ color: "#94a3b8", fontSize: "12px", fontWeight: "500" }}>32 fichas activas</span>
        </div>

        {/* Horarios Programados */}
        <div className={styles.statCard}>
          <div style={{ width: "42px", height: "42px", borderRadius: "10px", backgroundColor: "#ea580c", color: "white", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: "15px" }}>
            <Calendar size={22} strokeWidth={1.8} />
          </div>
          <p style={{ color: "#64748b", fontSize: "14px", fontWeight: "500", margin: "0 0 5px 0" }}>Horarios Programados</p>
          <div style={{ fontSize: "28px", fontWeight: "700", color: "#0f172a", margin: "0 0 5px 0" }}>312</div>
          <span style={{ color: "#94a3b8", fontSize: "12px", fontWeight: "500" }}>Esta semana</span>
        </div>
      </div>

      {/* 3. SECCIÓN INFERIOR */}
      <div className={styles.gridBottom}>
        
        {/* COLUMNA IZQUIERDA: HORARIOS */}
        <div className={styles.whiteBlock}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "25px" }}>
            <div style={{ textAlign: "left" }}>
              <div style={{ margin: "0 0 5px 0", fontSize: "18px", fontWeight: "600", color: "#0f172a", display: "flex", alignItems: "center", gap: "8px" }}>
                <Clock size={20} style={{ color: "#475569" }} /> Horario de Hoy
              </div>
              <p style={{ margin: 0, color: "#64748b", fontSize: "14px" }}>Clases programadas para hoy</p>
            </div>
            <button style={{ backgroundColor: "#16a34a", color: "white", padding: "10px 18px", borderRadius: "8px", fontWeight: "600", cursor: "pointer", fontSize: "14px", border: "none" }}>
              Ver Semana Completa
            </button>
          </div>

          {/* TARJETA DE CLASE 1 (08:00) */}
          <div className={styles.classCard}>
            {/* Contenedor de hora estilizado con verde menta suave e icono */}
            <div style={{ fontSize: "14px", fontWeight: "700", color: "#16a34a", padding: "12px 16px", borderRadius: "8px", backgroundColor: "#f0fdf4", display: "flex", flexDirection: "column", alignItems: "center", gap: "4px", minWidth: "75px" }}>
              <Clock size={16} strokeWidth={2.5} />
              <span>08:00</span>
            </div>
            
            <div style={{ flex: 1, textAlign: "left", paddingLeft: "5px" }}>
              {/* Ficha y Ambiente en la misma línea */}
              <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
                <span style={{ fontSize: "14px", fontWeight: "600", color: "#64748b" }}>2558963</span>
                <span style={{ backgroundColor: "#e0f2fe", color: "#0369a1", padding: "3px 8px", borderRadius: "6px", fontSize: "12px", fontWeight: "700" }}>Ambiente 301</span>
              </div>
              {/* Nombre del Programa */}
              <strong style={{ display: "block", fontSize: "16px", color: "#0f172a", fontWeight: "600", marginBottom: "6px" }}>
                Desarrollo de Software
              </strong>
              {/* Instructor con icono gris */}
              <span style={{ fontSize: "13px", color: "#64748b", display: "flex", alignItems: "center", gap: "6px" }}>
                <span style={{ color: "#94a3b8" }}>👤</span> Carlos Rodríguez
              </span>
            </div>
          </div>

          {/* TARJETA DE CLASE 2 (10:00) */}
          <div className={styles.classCard}>
            <div style={{ fontSize: "14px", fontWeight: "700", color: "#16a34a", padding: "12px 16px", borderRadius: "8px", backgroundColor: "#f0fdf4", display: "flex", flexDirection: "column", alignItems: "center", gap: "4px", minWidth: "75px" }}>
              <Clock size={16} strokeWidth={2.5} />
              <span>10:00</span>
            </div>
            
            <div style={{ flex: 1, textAlign: "left", paddingLeft: "5px" }}>
              <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
                <span style={{ fontSize: "14px", fontWeight: "600", color: "#64748b" }}>2558967</span>
                <span style={{ backgroundColor: "#e0f2fe", color: "#0369a1", padding: "3px 8px", borderRadius: "6px", fontSize: "12px", fontWeight: "700" }}>Ambiente 405</span>
              </div>
              <strong style={{ display: "block", fontSize: "16px", color: "#0f172a", fontWeight: "600", marginBottom: "6px" }}>
                Diseño Gráfico
              </strong>
              <span style={{ fontSize: "13px", color: "#64748b", display: "flex", alignItems: "center", gap: "6px" }}>
                <span style={{ color: "#94a3b8" }}>👤</span> Laura Gómez
              </span>
            </div>
          </div>
          {/*ACTIVIDAD RECIENTE */}
          <div className={styles.whiteBlock}>
            <div style={{ textAlign: "left", marginBottom: "20px" }}>
              <div style={{ margin: "0 0 5px 0", fontSize: "18px", fontWeight: "600", color: "#0f172a" }}>Actividad Reciente</div>
              <p style={{ margin: 0, color: "#64748b", fontSize: "14px" }}>Últimas actualizaciones en horarios</p>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
              
              {/* Ítem 1: En curso */}
              <div style={{ display: "flex", alignItems: "center", paddingBottom: "16px", borderBottom: "1px solid #f1f5f9" }}>
                <div style={{ width: "80px", height: "80px", borderRadius: "8px", backgroundColor: "#f0fdf4", color: "#16a34a", display: "flex", alignItems: "center", justifyContent: "center", marginRight: "16px" }}>
                  <CalendarCheck size={20} />
                </div>
                <div style={{ flex: 1, textAlign: "left" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "4px" }}>
                    <span style={{ fontSize: "14px", fontWeight: "500", color: "#334155" }}>Ficha 2558963</span>
                    <span style={{ backgroundColor: "#f1f5f9", color: "#334155", padding: "2px 6px", borderRadius: "4px", fontSize: "11px", fontWeight: "600" }}>Ambiente 301</span>
                  </div>
                  <div style={{ fontSize: "14px", fontWeight: "500", color: "#64748b", marginBottom: "4px" }}>Desarrollo de Software</div>
                  <div style={{ fontSize: "12px", color: "#94a3b8" }}>👤 Carlos Rodríguez &nbsp;•&nbsp; 🕒 08:00 - 12:00</div>
                </div>
                <span style={{ backgroundColor: "#ecfdf5", color: "#15803d", padding: "4px 10px", borderRadius: "20px", fontSize: "12px", fontWeight: "600" }}>En curso</span>
              </div>

              {/* Ítem 2: Programado */}
              <div style={{ display: "flex", alignItems: "center", paddingBottom: "16px", borderBottom: "1px solid #f1f5f9" }}>
                <div style={{ width: "80px", height: "80px", borderRadius: "8px", backgroundColor: "#f0fdf4", color: "#16a34a", display: "flex", alignItems: "center", justifyContent: "center", marginRight: "16px" }}>
                  <CalendarCheck size={20} />
                </div>
                <div style={{ flex: 1, textAlign: "left" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "4px" }}>
                    <span style={{ fontSize: "14px", fontWeight: "500", color: "#334155" }}>Ficha 2558964</span>
                    <span style={{ backgroundColor: "#f1f5f9", color: "#334155", padding: "2px 6px", borderRadius: "4px", fontSize: "11px", fontWeight: "600" }}>Ambiente 205</span>
                  </div>
                  <div style={{ fontSize: "14px", fontWeight: "500", color: "#64748b", marginBottom: "4px" }}>Gestión Administrativa</div>
                  <div style={{ fontSize: "12px", color: "#94a3b8" }}>👤 Ana Martínez &nbsp;•&nbsp; 🕒 14:00 - 18:00</div>
                </div>
                <span style={{ backgroundColor: "#f8fafc", color: "#475569", padding: "4px 10px", borderRadius: "20px", fontSize: "12px", fontWeight: "600", border: "1px solid #e2e8f0" }}>Programado</span>
              </div>

              {/* Ítem 3: Completado */}
              <div style={{ display: "flex", alignItems: "center" }}>
                <div style={{ width: "80px", height: "80px", borderRadius: "8px", backgroundColor: "#f0fdf4", color: "#16a34a", display: "flex", alignItems: "center", justifyContent: "center", marginRight: "16px" }}>
                  <CalendarCheck size={20} />
                </div>
                <div style={{ flex: 1, textAlign: "left" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "4px" }}>
                    <span style={{ fontSize: "14px", fontWeight: "500", color: "#334155" }}>Ficha 2558965</span>
                    <span style={{ backgroundColor: "#f1f5f9", color: "#334155", padding: "2px 6px", borderRadius: "4px", fontSize: "11px", fontWeight: "600" }}>Ambiente 102</span>
                  </div>
                  <div style={{ fontSize: "14px", fontWeight: "500", color: "#64748b", marginBottom: "4px" }}>Contabilidad y Finanzas</div>
                  <div style={{ fontSize: "12px", color: "#94a3b8" }}>👤 María López &nbsp;•&nbsp; 🕒 08:00 - 12:00</div>
                </div>
                <span style={{ backgroundColor: "#f1f5f9", color: "#64748b", padding: "4px 10px", borderRadius: "20px", fontSize: "12px", fontWeight: "600" }}>Completado</span>
              </div>

            </div>

        </div>
        </div>
        {/* COLUMNA DERECHA: ACCIONES RÁPIDAS */}
        <div className={styles.whiteBlock}>
          <div style={{ textAlign: "left", marginBottom: "20px" }}>
            <div style={{ margin: "0 0 5px 0", fontSize: "18px", fontWeight: "600", color: "#0f172a" }}>Acciones Rápidas</div>
            <p style={{ margin: 0, color: "#64748b", fontSize: "14px" }}>Gestión del sistema</p>
          </div>

          {/* Crear Horario */}
          <button className={styles.actionBtn} style={{ backgroundColor: "#2563eb", marginBottom: "12px" }}>
            <Calendar size={22} strokeWidth={1.8} />
            <div style={{ textAlign: "left", flex: 1 }}>
              <strong style={{ display: "block", fontSize: "15px" }}>Crear Horario</strong>
              <small style={{ display: "block", opacity: 0.9, fontSize: "12px", color: "rgba(255,255,255,0.8)" }}>Nueva programación</small>
            </div>
            <ChevronRight size={18} />
          </button>

          {/* Gestionar Ambientes */}
          <button className={styles.actionBtn} style={{ backgroundColor: "#16a34a", marginBottom: "12px" }}>
            <Building2 size={22} strokeWidth={1.8} />
            <div style={{ textAlign: "left", flex: 1 }}>
              <strong style={{ display: "block", fontSize: "15px" }}>Gestionar Ambientes</strong>
              <small style={{ display: "block", opacity: 0.9, fontSize: "12px", color: "rgba(255,255,255,0.8)" }}>Ver disponibilidad</small>
            </div>
            <ChevronRight size={18} />
          </button>

          {/* Instructores */}
          <button className={styles.actionBtn} style={{ backgroundColor: "#7c3aed" }}>
            <UserCheck size={22} strokeWidth={1.8} />
            <div style={{ textAlign: "left", flex: 1 }}>
              <strong style={{ display: "block", fontSize: "15px" }}>Instructores</strong>
              <small style={{ display: "block", opacity: 0.9, fontSize: "12px", color: "rgba(255,255,255,0.8)" }}>Ver asignaciones</small>
            </div>
            <ChevronRight size={18} />
          </button>
        
          {/* Fichas */}
          <button className={styles.actionBtn} style={{ backgroundColor: "#7c3aed" }}>
            <GraduationCap size={22} strokeWidth={1.8} />
            <div style={{ textAlign: "left", flex: 1 }}>
              <strong style={{ display: "block", fontSize: "15px" }}>Fichas</strong>
              <small style={{ display: "block", opacity: 0.9, fontSize: "12px", color: "rgba(255,255,255,0.8)" }}>Gestionar grupos</small>
            </div>
            <ChevronRight size={18} />
          </button>
        </div>  

      </div>
    </div>
  );
}