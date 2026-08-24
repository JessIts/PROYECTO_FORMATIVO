import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import Login from "../pages/Login";

import RegisterRole from "../pages/RegisterRole";
import RegisterForm from "../pages/RegisterForm";
import SetPassword from "../pages/SetPassword";
import ForgotPassword from "../pages/ForgotPassword";
import ResetPassword from "../pages/ResetPassword";

import Dashboard from "../pages/Dashboard/Dashboard";

import ProtectedRoute from "./ProtectedRoute";

export default function AppRouter() {

  return (
    <BrowserRouter>

      <Routes>

        {/* 🔐 LOGIN */}
        <Route
          path="/"
          element={<Login />}
        />

        {/* 📊 DASHBOARD PROTEGIDO */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        {/* 🔑 RECUPERACIÓN */}
        <Route
          path="/forgot-password"
          element={<ForgotPassword />}
        />

        <Route
          path="/reset-password"
          element={<ResetPassword />}
        />

        {/* 👤 REGISTRO */}
        <Route
          path="/register-role"
          element={<RegisterRole />}
        />

        <Route
          path="/register-form"
          element={<RegisterForm />}
        />

        {/* 🔐 PASSWORD FINAL */}
        <Route
          path="/set-password"
          element={<SetPassword />}
        />

        {/* ❌ RUTA NO ENCONTRADA */}
        <Route
          path="*"
          element={
            <Navigate
              to="/"
              replace
            />
          }
        />

      </Routes>

    </BrowserRouter>
  );
}