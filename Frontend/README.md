FRONTEND – DESARROLLO DEL PROYECTO

En mi parte del proyecto me correspondió el desarrollo del frontend, el cual es la interfaz visual del sistema donde el usuario interactúa directamente.

Durante este proceso estuve trabajando en tres módulos principales:

 Login de usuarios
 Registro de usuarios
 Recuperación de contraseña

Cada uno de estos módulos fue desarrollado cumpliendo con los requerimientos establecidos en el proyecto, incluyendo validaciones de formularios,

¿CÓMO SE LEVANTA EL PROYECTO FRONTEND?

Para ejecutar el proyecto en mi computador se utilizaron los siguientes comandos:

 1. Crear el proyecto con React + Vite
    
npm create vite@latest frontend

 3. Entrar a la carpeta del proyecto
    
cd frontend

 5. Instalar dependencias del proyecto
    
npm install

 7. Instalar librerías necesarias
    
npm install react-router-dom lucide-react react-i18next i18next

 9. Ejecutar el proyecto en modo desarrollo
     
npm run dev

 11. Acceder al proyecto en el navegador

Después de ejecutar el comando, el sistema se abre en:

http://localhost:5174


3. ¿Qué es React?

React es una librería de JavaScript que permite construir interfaces de usuario modernas basadas en componentes reutilizables.

Ejemplo de componentes en este proyecto:

LoginPage

RegisterPage

ForgotPasswordPage

InputField

Button


CONEXIÓN CON EL BACKEND

El frontend se conecta con el backend mediante peticiones HTTP (API REST), donde se envían los datos ingresados por el usuario (correo, contraseña, etc.) y el backend responde con información como:

Validación de usuario

Mensajes de error

Token de autenticación


¿Cómo se comunican frontend y backend?

El frontend se comunica con el backend mediante peticiones (requests), enviando datos y recibiendo respuestas.

Ejemplo:

El usuario escribe correo y contraseña
El frontend envía esos datos al backend
El backend valida la información
El backend responde si el acceso es correcto o incorrecto



TECNOLOGÍAS UTILIZADAS

 
 
React (interfaz de usuario)

Vite (entorno de desarrollo)

JavaScript / TypeScript

React Router DOM (navegación entre páginas)

Lucide React (íconos)

i18next (multilenguaje)




FUNCIONALIDADES DEL FRONTEND

 
Validación de formularios en login y registro

Manejo de errores en pantalla

Control de contraseñas seguras

Recuperación de contraseña por pasos

Navegación entre páginas

Diseño responsivo (adaptable a celular y PC)

