CREATE DATABASE sistema_SIHS;
USE sistema_SIHS;

CREATE TABLE coordinaciones (
	idCoordinacion CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	nombreCoordinacion VARCHAR(50) NOT NULL
);

CREATE TABLE programasDeFormacion (
	idPrograma CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	nombrePrograma VARCHAR(50) NOT NULL,
	nivelDeFormacion ENUM ('tecnico','tecnologo','operario') NOT NULL,
	tipoDeOferta ENUM ('abierta','cerrada') NOT NULL,
	estado ENUM ('en formacion', 'finalizado') NOT NULL,
	idCoordinacion CHAR(36) NOT NULL,
	FOREIGN KEY (idCoordinacion) REFERENCES coordinaciones(idCoordinacion)
);

CREATE TABLE usuarios(
	idUsuario CHAR(36) PRIMARY KEY DEFAULT (UUID()), 
	nombresUsuario VARCHAR(100) NOT NULL,
	apellidosUsuario VARCHAR(100) NOT NULL,
	tipoDocumento ENUM ('CC','CE','PPT','TI'),
	documentoUsuario VARCHAR(50) NOT NULL UNIQUE,
	correoUsuario VARCHAR(50) NOT NULL,
	telefonoUsuario VARCHAR(15) NOT NULL,
	contrasenaUsuario VARCHAR(256) NOT NULL
);

CREATE TABLE fichas (
	idFicha VARCHAR (50) PRIMARY KEY NOT NULL,
	idPrograma CHAR(36) NOT NULL,
	cantidadAprendices INT NOT NULL,
	FOREIGN KEY (idPrograma) REFERENCES programasDeFormacion(idPrograma)
);

CREATE TABLE trimestre (
	idTrimestre CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	numeroTrimestre VARCHAR(10) NOT NULL,
	fechaInicioTrimestre DATE NOT NULL,
	fechaFinTrimestre DATE NOT NULL,
	idPrograma CHAR(36) NOT NULL,
	FOREIGN KEY (idPrograma) REFERENCES programasDeFormacion(idPrograma)
);

CREATE TABLE aprendices (
	idAprendiz CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	documentoUsuario VARCHAR(50) NOT NULL,
	idFicha VARCHAR (50) NOT NULL,
	FOREIGN KEY (documentoUsuario) REFERENCES usuarios(documentoUsuario),
	FOREIGN KEY (idFicha) REFERENCES fichas(idFicha)
);

CREATE TABLE instructores (
	idInstructor CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	documentoUsuario VARCHAR(50) NOT NULL,
	especialidadInstructor VARCHAR(30) NOT NULL,
	tipoDeContrato ENUM ('planta','contratista') NOT NULL,
	FOREIGN KEY (documentoUsuario) REFERENCES usuarios(documentoUsuario)
);

CREATE TABLE ambientesDeFormacion (
	idAmbiente CHAR(36) PRIMARY KEY DEFAULT (UUID()),
	nombreAmbiente VARCHAR(20) NOT NULL,
	tipoDeAmbiente ENUM ('Especial','Regular') NOT NULL,
	sede ENUM ('1','2','3','4') NOT NULL
);

CREATE TABLE resultadosDeAprendizaje (
	idResultadoDeAprendizaje VARCHAR (50) PRIMARY KEY NOT NULL,
	idTrimestre CHAR(36) NOT NULL,
	FOREIGN KEY (idTrimestre) REFERENCES trimestre(idTrimestre)
);

CREATE TABLE horarios (
	idHorario CHAR (36) NOT NULL PRIMARY KEY DEFAULT (UUID()),
    idFicha JSON NOT NULL,
    idInstructor JSON NOT NULL,
    idAmbiente JSON NOT NULL,
    dias JSON NOT NULL,
    jornadas JSON NOT NULL,
    idTrimestre JSON NOT NULL
);
-- nota: esta tabla "horarios" es mejor plantearla en una base de datos no relacional