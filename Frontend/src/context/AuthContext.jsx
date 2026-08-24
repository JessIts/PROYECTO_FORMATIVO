import {
    createContext,
    useContext,
    useEffect,
    useState
} from "react";

const AuthContext = createContext(null);

const API_URL = "http://localhost:8000";

export function AuthProvider({ children }) {

    const [token, setToken] = useState(
        () => localStorage.getItem("token")
    );

    const [user, setUser] = useState(null);

    const [loading, setLoading] = useState(true);


    // ============================================================
    // LIMPIAR SESIÓN
    // ============================================================

    const clearSession = () => {
        localStorage.removeItem("token");

        setToken(null);
        setUser(null);
    };


    // ============================================================
    // OBTENER USUARIO AUTENTICADO
    // ============================================================

    const fetchCurrentUser = async (currentToken) => {

        try {

            const response = await fetch(
                `${API_URL}/auth/me`,
                {
                    method: "GET",

                    headers: {
                        Authorization: `Bearer ${currentToken}`
                    }
                }
            );

            if (!response.ok) {
                throw new Error("Token inválido o expirado");
            }

            const data = await response.json();

            setUser(data);

            return data;

        } catch (error) {

            console.error(
                "Error obteniendo usuario:",
                error
            );

            clearSession();

            return null;
        }
    };


    // ============================================================
    // CARGAR USUARIO AL INICIAR LA APLICACIÓN
    // ============================================================

    useEffect(() => {

        const loadUser = async () => {

            if (!token) {
                setLoading(false);
                return;
            }

            await fetchCurrentUser(token);

            setLoading(false);
        };

        loadUser();

    }, [token]);


    // ============================================================
    // LOGIN
    // ============================================================

    const login = async (loginData) => {

        const response = await fetch(
            `${API_URL}/auth/login`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(loginData)
            }
        );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Error al iniciar sesión"
            );
        }

        localStorage.setItem(
            "token",
            data.access_token
        );

        setToken(data.access_token);

        return data;
    };


    // ============================================================
    // LOGOUT
    // ============================================================

    const logout = () => {
        clearSession();
    };


    // ============================================================
    // VALOR DEL CONTEXT
    // ============================================================

    const value = {
        token,
        user,
        loading,
        login,
        logout,
        isAuthenticated: !!token
    };


    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}


// ============================================================
// HOOK
// ============================================================

export function useAuth() {

    const context = useContext(AuthContext);

    if (!context) {

        throw new Error(
            "useAuth debe utilizarse dentro de AuthProvider"
        );
    }

    return context;
}