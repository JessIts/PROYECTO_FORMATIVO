const API_URL = "http://localhost:8000";

const handleResponse = async (res) => {
  const data = await res.json();

  if (!res.ok) {
    const error = new Error(
      data?.detail ||
      data?.message ||
      "Error en la petición"
    );

    error.status = res.status;

    throw error;
  }

  return data;
};


// ============================================================
// LOGIN
// ============================================================

export const loginRequest = async (data) => {

  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return handleResponse(res);
};


// ============================================================
// REGISTRO
// ============================================================

export const registerRequest = async (data) => {

  const res = await fetch(`${API_URL}/usuarios/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return handleResponse(res);
};


// ============================================================
// FORGOT PASSWORD
// ============================================================

export const forgotPasswordRequest = async (data) => {

  const res = await fetch(`${API_URL}/auth/forgot-password`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return handleResponse(res);
};


// ============================================================
// RESET PASSWORD
// ============================================================

export const resetPasswordRequest = async (data) => {

  const res = await fetch(`${API_URL}/auth/reset-password`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return handleResponse(res);
};


// ============================================================
// SET PASSWORD
// ============================================================

export const setPasswordRequest = async (data) => {

  const res = await fetch(`${API_URL}/auth/set-password`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return handleResponse(res);
};

// ============================================================
// OBTENER USUARIO AUTENTICADO
// ============================================================

export const getCurrentUserRequest = async () => {

  const token = localStorage.getItem("token");

  const res = await fetch(`${API_URL}/auth/me`, {
    method: "GET",

    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return handleResponse(res);
};