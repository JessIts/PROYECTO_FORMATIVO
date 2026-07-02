import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import Login from "../pages/Login";
import RegisterRole from "../pages/RegisterRole";
import RegisterForm from "../pages/RegisterForm";
import SetPassword from "../pages/SetPassword";
import ForgotPassword from "../pages/ForgotPassword";
import ResetPassword from "../pages/ResetPassword";
import Dashboard from "../pages/Dashboard/Dashboard";

export default function AppRouter() {
  return (
    <BrowserRouter>
    
      <Routes>
        
        {/* 🔐 LOGIN */}
        <Route path="/" element={<Login />} />

        {/* 📊 DASHBOARD (Llamado directo, sin envoltorios obsoletos) */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* 🔑 RECUPERACIÓN */}
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password" element={<ResetPassword />} />

        {/* 👤 REGISTRO */}
        <Route path="/register-role" element={<RegisterRole />} />
        <Route path="/register-form" element={<RegisterForm />} />

        {/* 🔐 PASSWORD FINAL */}
        <Route path="/set-password" element={<SetPassword />} />

        {/* ❌ RUTA NO ENCONTRADA */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}