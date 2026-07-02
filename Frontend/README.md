# FRONTEND (REACT)

Frontend del Sistema Integrado de Horarios (SIHS), desarrollado en React para la gestión de autenticación, registro de usuarios y recuperación de contraseña.

---

#  Tecnologías utilizadas

-Framework: React JS
-Build Tool: Vite
-Navegación: React Router DOM
-Lenguaje: JavaScript (ES6+)
-Estilos: CSS3 (Implementación de CSS Modules para encapsulamiento)
-Comunicación: Fetch API (Consumo de servicios REST FastAPI)

---

#  Estructura del proyecto

```
src/
├── api/
│   └── auth.api.js
├── assets/
│   ├── hero.png
│   ├── react.svg
│   └── vite.svg
├── components/
│   ├── InputField.jsx
│   ├── Navbar.jsx
│   └── ProtectedRoute.jsx
├── context/
│   └── AuthContext.jsx
├── pages/
│   ├── Dashboard/
│   │   ├── Dashboard.jsx
│   │   ├── Dashboard.module.css
│   │   ├── ViewCoordinator.jsx
│   │   ├── ViewInstructor.jsx
│   │   └── ViewLearner.jsx
│   ├── ForgotPassword.jsx
│   ├── Login.jsx
│   ├── RegisterForm.jsx
│   ├── RegisterRole.jsx
│   ├── ResetPassword.jsx
│   └── SetPassword.jsx
├── routes/
│   └── AppRouter.jsx
├── App.css
├── App.jsx
├── auth.css
├── index.css
└── main.jsx
```

---

#  Instalación del proyecto (DESDE CERO)

## 1️ Instalar Node.js
Descargar e instalar Node.js:
https://nodejs.org/

Verificar instalación:

```bash
node -v
npm -v
```

---

## 2️ Crear proyecto React con Vite

```bash
npm create vite@latest frontend
```

Seleccionar:
- React
- JavaScript

---

## 3️ Entrar al proyecto

```bash
cd frontend
```

---

## 4️ Instalar dependencias

```bash
npm install
```

---

## 5️ Instalar React Router DOM

```bash
npm install react-router-dom
```

---

## 6️ Ejecutar proyecto

```bash
npm run dev
```

---


#  Módulos del sistema

##  Login
- Autenticación de usuario
- Generación de token

Endpoint:
```
POST /auth/login
```

---

##  Registro de usuarios
- Registro por roles:
  - Coordinador
  - Instructor
  - Aprendiz

Endpoint:
```
POST /auth/register
```

---

##  Recuperación de contraseña
Flujo:

1. Enviar correo
2. Validar código (modal)
3. Nueva contraseña

Endpoints:
```
POST /auth/forgot-password
POST /auth/reset-password
```

---

##  Set password
Validación de contraseña segura:

- Mayúscula
- Minúscula
- Número
- Carácter especial
- Mínimo 8 caracteres

Endpoint:
```
POST /auth/set-password
```

---

# Rutas del frontend

```text
/               → Login
/register-role  → Selección de rol
/register-form  → Registro
/set-password   → Crear contraseña
/forgot-password→ Recuperación
/reset          → Reset password
/dashboard      → Dashboard Principal (Vista dinámica según rol)
```

---


# Validaciones y Arquitectura

- Campos obligatorios
- Validación de contraseña segura
- Confirmación de contraseña
- Validación por rol
- Control de formularios
- Arquitectura modular (CSS Modules)
- Iconografía estilizada (Lucide React)
---


#  Flujo del sistema

```
Login 
  ↓
Registro 
  ↓
Set Password 
  ↓
Login 
  ↓
Dashboard (Vista dinámica según rol)
```

---

# ▶ Ejecución

```bash
npm install
npm run dev
```

---

# 🌐 URL del proyecto

```
http://localhost:5173
```

---

#  Estado del proyecto

✔ Login funcional  
✔ Registro por roles  
✔ Recuperación de contraseña con modal  
✔ Set password seguro  
✔ Rutas configuradas  
✔ Consumo de API REST  

---

# 
