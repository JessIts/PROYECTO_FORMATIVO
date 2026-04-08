CREATE DATABASE sistema_SIHS;
USE sistema_SIHS;

-- =========================
-- ROLES Y USUARIOS
-- =========================
CREATE TABLE roles (
    idRol INT PRIMARY KEY AUTO_INCREMENT,
    nombreRol VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE usuarios (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    estado ENUM('activo','inactivo') DEFAULT 'activo',
    fechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usuario_rol (
    idUsuario INT,
    idRol INT,
    PRIMARY KEY (idUsuario, idRol),
    FOREIGN KEY (idUsuario) REFERENCES usuarios(idUsuario),
    FOREIGN KEY (idRol) REFERENCES roles(idRol)
);

-- =========================
-- ESTRUCTURA ACADÉMICA
-- =========================
CREATE TABLE coordinaciones (
    idCoordinacion INT PRIMARY KEY AUTO_INCREMENT,
    nombreCoordinacion VARCHAR(100)
);

CREATE TABLE programas (
    idPrograma INT PRIMARY KEY AUTO_INCREMENT,
    nombrePrograma VARCHAR(100),
    idCoordinacion INT,
    FOREIGN KEY (idCoordinacion) REFERENCES coordinaciones(idCoordinacion)
);

CREATE TABLE fichas (
    idFicha INT PRIMARY KEY AUTO_INCREMENT,
    codigoFicha VARCHAR(50) UNIQUE,
    idPrograma INT,
    FOREIGN KEY (idPrograma) REFERENCES programas(idPrograma)
);

CREATE TABLE trimestres (
    idTrimestre INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    estado ENUM('planeado','activo','finalizado') DEFAULT 'planeado'
);

-- =========================
-- COMPETENCIAS / RESULTADOS / ACTIVIDADES
-- =========================
CREATE TABLE competencias_formacion (
    idCompetencia INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(50),
    descripcion TEXT NOT NULL,
    idPrograma INT NOT NULL,
    FOREIGN KEY (idPrograma) REFERENCES programas(idPrograma)
);

CREATE TABLE resultados_aprendizaje (
    idResultado INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(50),
    descripcion TEXT NOT NULL,
    idCompetencia INT NOT NULL,
    FOREIGN KEY (idCompetencia)
        REFERENCES competencias_formacion(idCompetencia)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE actividades_aprendizaje (
    idActividad INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(50),
    descripcion TEXT NOT NULL,
    tipoActividad VARCHAR(80),
    duracionMinutos INT,
    idResultado INT NOT NULL,
    FOREIGN KEY (idResultado)
        REFERENCES resultados_aprendizaje(idResultado)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================
-- FICHA - USUARIO
-- =========================
CREATE TABLE ficha_usuario (
    idFicha INT,
    idUsuario INT,
    PRIMARY KEY (idFicha, idUsuario),
    FOREIGN KEY (idFicha) REFERENCES fichas(idFicha),
    FOREIGN KEY (idUsuario) REFERENCES usuarios(idUsuario)
);

-- =========================
-- SEDES Y AMBIENTES
-- =========================
CREATE TABLE sedes (
    idSede INT PRIMARY KEY AUTO_INCREMENT,
    nombreSede VARCHAR(100),
    direccion VARCHAR(150),
    tipoSede ENUM('principal','secundaria','alterna')
);

CREATE TABLE ambientes (
    idAmbiente INT PRIMARY KEY AUTO_INCREMENT,
    nombreAmbiente VARCHAR(50),
    idSede INT,
    FOREIGN KEY (idSede) REFERENCES sedes(idSede)
);

-- =========================
-- JORNADAS
-- =========================
CREATE TABLE jornadas (
    idJornada INT PRIMARY KEY AUTO_INCREMENT,
    nombreJornada VARCHAR(50)
);

-- =========================
-- HORARIOS
-- =========================
CREATE TABLE diasDeLaSemana (
    idDia INT PRIMARY KEY AUTO_INCREMENT,
    nombreDia VARCHAR(10) UNIQUE
);

CREATE TABLE horarios (
    idHorario INT PRIMARY KEY AUTO_INCREMENT,
    horaInicio TIME,
    horaFin TIME,
    idJornada INT,
    FOREIGN KEY (idJornada) REFERENCES jornadas(idJornada)
);

CREATE TABLE horario_dia (
    idHorario INT,
    idDia INT,
    PRIMARY KEY (idHorario, idDia),
    FOREIGN KEY (idHorario) REFERENCES horarios(idHorario),
    FOREIGN KEY (idDia) REFERENCES diasDeLaSemana(idDia)
);

-- =========================
-- PROGRAMACIÓN
-- =========================