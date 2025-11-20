-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2025 a las 17:06:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_horarios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ambiente`
--

CREATE TABLE `ambiente` (
  `id_ambiente` int(11) NOT NULL,
  `numero_ambiente` varchar(20) NOT NULL,
  `sede` varchar(100) NOT NULL,
  `tipo` enum('Regular','Especial') NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `estado` enum('Disponible','Ocupado','Mantenimiento') DEFAULT 'Disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aprendiz`
--

CREATE TABLE `aprendiz` (
  `id_aprendiz` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `codigo_ficha` int(11) NOT NULL,
  `programa_formación` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigo_instructor`
--

CREATE TABLE `codigo_instructor` (
  `id_codigo` int(11) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `usado` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coordinador`
--

CREATE TABLE `coordinador` (
  `id_coordinador` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ficha`
--

CREATE TABLE `ficha` (
  `id_ficha` int(11) NOT NULL,
  `numero_ficha` varchar(30) NOT NULL,
  `jornada` enum('M','T','N') NOT NULL,
  `programa_formación` varchar(120) NOT NULL,
  `area` enum('Técnico','Tecnólogo') NOT NULL,
  `nivel` varchar(30) DEFAULT NULL,
  `trimestre_actual` int(11) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin_lectiva` date DEFAULT NULL,
  `fecha_fin_productiva` date DEFAULT NULL,
  `cantidad_aprendices` int(11) DEFAULT NULL,
  `estado` enum('Activa','Inactiva','Finalizada') DEFAULT 'Activa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `id_horario` int(11) NOT NULL,
  `id_ficha` int(11) NOT NULL,
  `id_instructor` int(11) NOT NULL,
  `id_ambiente` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `jornada` enum('M','T','N') NOT NULL,
  `bloque` int(11) DEFAULT NULL CHECK (`bloque` in (1,2)),
  `horas_programadas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario_resultado`
--

CREATE TABLE `horario_resultado` (
  `id_hr` int(11) NOT NULL,
  `id_horario` int(11) NOT NULL,
  `id_resultado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instructor`
--

CREATE TABLE `instructor` (
  `id_instructor` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `codigo_instructor` varchar(20) NOT NULL,
  `especialidad` varchar(80) DEFAULT NULL,
  `tipo_contrato` enum('Planta','Contrato') NOT NULL,
  `horas_max` int(11) DEFAULT NULL CHECK (`horas_max` in (32,40))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recuperacion`
--

CREATE TABLE `recuperacion` (
  `id_recuperacion` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  `fecha_envio` datetime NOT NULL,
  `expiracion` datetime NOT NULL,
  `usado` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado`
--

CREATE TABLE `resultado` (
  `id_resultado` int(11) NOT NULL,
  `codigo_resultado` varchar(20) NOT NULL,
  `nombre_resultado` varchar(200) NOT NULL,
  `trimestre` int(11) NOT NULL,
  `programa_formación` varchar(120) NOT NULL,
  `horas_requeridas` int(11) NOT NULL,
  `acronimo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `tipo_usuario` enum('Coordinador','Instructor','Aprendiz','Admin') NOT NULL,
  `nombres` varchar(80) NOT NULL,
  `apellidos` varchar(80) NOT NULL,
  `nro_documento` varchar(30) NOT NULL,
  `tipo_documento` varchar(20) NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `contraseña` varchar(255) NOT NULL,
  `estado` enum('Activo','Bloqueado') DEFAULT 'Activo',
  `intentos_login` int(11) DEFAULT 0,
  `verificado_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `validacion_aprendiz`
--

CREATE TABLE `validacion_aprendiz` (
  `id_val` int(11) NOT NULL,
  `nombres` varchar(80) DEFAULT NULL,
  `apellidos` varchar(80) DEFAULT NULL,
  `codigo_ficha` int(11) NOT NULL,
  `programa_formación` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  ADD PRIMARY KEY (`id_ambiente`),
  ADD UNIQUE KEY `numero_ambiente` (`numero_ambiente`,`sede`);

--
-- Indices de la tabla `aprendiz`
--
ALTER TABLE `aprendiz`
  ADD PRIMARY KEY (`id_aprendiz`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `codigo_ficha` (`codigo_ficha`);

--
-- Indices de la tabla `codigo_instructor`
--
ALTER TABLE `codigo_instructor`
  ADD PRIMARY KEY (`id_codigo`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `coordinador`
--
ALTER TABLE `coordinador`
  ADD PRIMARY KEY (`id_coordinador`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `ficha`
--
ALTER TABLE `ficha`
  ADD PRIMARY KEY (`id_ficha`),
  ADD UNIQUE KEY `numero_ficha` (`numero_ficha`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`),
  ADD UNIQUE KEY `id_ficha` (`id_ficha`,`fecha`,`jornada`,`bloque`),
  ADD KEY `id_instructor` (`id_instructor`),
  ADD KEY `id_ambiente` (`id_ambiente`);

--
-- Indices de la tabla `horario_resultado`
--
ALTER TABLE `horario_resultado`
  ADD PRIMARY KEY (`id_hr`),
  ADD KEY `id_horario` (`id_horario`),
  ADD KEY `id_resultado` (`id_resultado`);

--
-- Indices de la tabla `instructor`
--
ALTER TABLE `instructor`
  ADD PRIMARY KEY (`id_instructor`),
  ADD UNIQUE KEY `codigo_instructor` (`codigo_instructor`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `recuperacion`
--
ALTER TABLE `recuperacion`
  ADD PRIMARY KEY (`id_recuperacion`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `resultado`
--
ALTER TABLE `resultado`
  ADD PRIMARY KEY (`id_resultado`),
  ADD UNIQUE KEY `codigo_resultado` (`codigo_resultado`),
  ADD UNIQUE KEY `nombre_resultado` (`nombre_resultado`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `nro_documento` (`nro_documento`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indices de la tabla `validacion_aprendiz`
--
ALTER TABLE `validacion_aprendiz`
  ADD PRIMARY KEY (`id_val`),
  ADD KEY `codigo_ficha` (`codigo_ficha`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  MODIFY `id_ambiente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `aprendiz`
--
ALTER TABLE `aprendiz`
  MODIFY `id_aprendiz` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `codigo_instructor`
--
ALTER TABLE `codigo_instructor`
  MODIFY `id_codigo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `coordinador`
--
ALTER TABLE `coordinador`
  MODIFY `id_coordinador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ficha`
--
ALTER TABLE `ficha`
  MODIFY `id_ficha` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horario_resultado`
--
ALTER TABLE `horario_resultado`
  MODIFY `id_hr` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `instructor`
--
ALTER TABLE `instructor`
  MODIFY `id_instructor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `recuperacion`
--
ALTER TABLE `recuperacion`
  MODIFY `id_recuperacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `resultado`
--
ALTER TABLE `resultado`
  MODIFY `id_resultado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `validacion_aprendiz`
--
ALTER TABLE `validacion_aprendiz`
  MODIFY `id_val` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `aprendiz`
--
ALTER TABLE `aprendiz`
  ADD CONSTRAINT `aprendiz_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  ADD CONSTRAINT `aprendiz_ibfk_2` FOREIGN KEY (`codigo_ficha`) REFERENCES `ficha` (`id_ficha`);

--
-- Filtros para la tabla `codigo_instructor`
--
ALTER TABLE `codigo_instructor`
  ADD CONSTRAINT `codigo_instructor_ibfk_1` FOREIGN KEY (`codigo`) REFERENCES `instructor` (`codigo_instructor`);

--
-- Filtros para la tabla `coordinador`
--
ALTER TABLE `coordinador`
  ADD CONSTRAINT `coordinador_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `horario_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha` (`id_ficha`),
  ADD CONSTRAINT `horario_ibfk_2` FOREIGN KEY (`id_instructor`) REFERENCES `instructor` (`id_instructor`),
  ADD CONSTRAINT `horario_ibfk_3` FOREIGN KEY (`id_ambiente`) REFERENCES `ambiente` (`id_ambiente`);

--
-- Filtros para la tabla `horario_resultado`
--
ALTER TABLE `horario_resultado`
  ADD CONSTRAINT `horario_resultado_ibfk_1` FOREIGN KEY (`id_horario`) REFERENCES `horario` (`id_horario`),
  ADD CONSTRAINT `horario_resultado_ibfk_2` FOREIGN KEY (`id_resultado`) REFERENCES `resultado` (`id_resultado`);

--
-- Filtros para la tabla `instructor`
--
ALTER TABLE `instructor`
  ADD CONSTRAINT `instructor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `recuperacion`
--
ALTER TABLE `recuperacion`
  ADD CONSTRAINT `recuperacion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `validacion_aprendiz`
--
ALTER TABLE `validacion_aprendiz`
  ADD CONSTRAINT `validacion_aprendiz_ibfk_1` FOREIGN KEY (`codigo_ficha`) REFERENCES `ficha` (`id_ficha`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
