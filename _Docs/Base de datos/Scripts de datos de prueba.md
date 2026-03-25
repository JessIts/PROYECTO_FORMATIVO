INSERT INTO coordinaciones (idCoordinacion, nombreCoordinacion) VALUES
(UUID(), 'Teleinformatica'),
(UUID(), 'Logistica'),
(UUID(), 'Artes');

INSERT INTO programasDeFormacion 
(idPrograma, nombrePrograma, nivelDeFormacion, tipoDeOferta, estado, idCoordinacion)
SELECT UUID(), 'Analisis y Desarrollo de Software', 'tecnologo', 'abierta', 'en formacion', idCoordinacion
FROM coordinaciones WHERE nombreCoordinacion = 'Teleinformatica';

INSERT INTO programasDeFormacion 
(idPrograma, nombrePrograma, nivelDeFormacion, tipoDeOferta, estado, idCoordinacion)
SELECT UUID(), 'Mantenimiento Industrial', 'tecnico', 'cerrada', 'en formacion', idCoordinacion
FROM coordinaciones WHERE nombreCoordinacion = 'Logistica';

INSERT INTO usuarios 
(idUsuario, nombresUsuario, apellidosUsuario, tipoDocumento, documentoUsuario, correoUsuario, telefonoUsuario, contrasenaUsuario)
VALUES
(UUID(), 'Juan', 'Perez', 'CC', '1001', 'juan@mail.com', '3001111111', 'hash1'),
(UUID(), 'Maria', 'Gomez', 'CC', '1002', 'maria@mail.com', '3002222222', 'hash2'),
(UUID(), 'Carlos', 'Lopez', 'CE', '1003', 'carlos@mail.com', '3003333333', 'hash3'),
(UUID(), 'Ana', 'Martinez', 'TI', '1004', 'ana@mail.com', '3004444444', 'hash4');

INSERT INTO fichas (idFicha, idPrograma, cantidadAprendices)
SELECT 'F001', idPrograma, 25 FROM programasDeFormacion 
WHERE nombrePrograma = 'Analisis y Desarrollo de Software';

INSERT INTO fichas (idFicha, idPrograma, cantidadAprendices)
SELECT 'F002', idPrograma, 20 FROM programasDeFormacion 
WHERE nombrePrograma = 'Mantenimiento Industrial';

INSERT INTO trimestre 
(idTrimestre, numeroTrimestre, fechaInicioTrimestre, fechaFinTrimestre, idPrograma)
SELECT UUID(), '1', '2026-01-01', '2026-03-31', idPrograma 
FROM programasDeFormacion 
WHERE nombrePrograma = 'Analisis y Desarrollo de Software';

INSERT INTO trimestre 
(idTrimestre, numeroTrimestre, fechaInicioTrimestre, fechaFinTrimestre, idPrograma)
SELECT UUID(), '1', '2026-04-01', '2026-06-30', idPrograma 
FROM programasDeFormacion 
WHERE nombrePrograma = 'Mantenimiento Industrial';

INSERT INTO aprendices (idAprendiz, documentoUsuario, idFicha) VALUES
(UUID(), '1001', 'F001'),
(UUID(), '1002', 'F001');

INSERT INTO instructores 
(idInstructor, documentoUsuario, especialidadInstructor, tipoDeContrato)
VALUES
(UUID(), '1003', 'Programacion', 'planta'),
(UUID(), '1004', 'Mecanica', 'contratista');

INSERT INTO ambientesDeFormacion 
(idAmbiente, nombreAmbiente, tipoDeAmbiente, sede)
VALUES
(UUID(), 'Lab Sistemas', 'Especial', '1'),
(UUID(), 'Taller Industrial', 'Especial', '2');

INSERT INTO resultadosDeAprendizaje (idResultadoDeAprendizaje, idTrimestre)
SELECT 'RA001', idTrimestre FROM trimestre LIMIT 1;

INSERT INTO resultadosDeAprendizaje (idResultadoDeAprendizaje, idTrimestre)
SELECT 'RA002', idTrimestre FROM trimestre LIMIT 1;

INSERT INTO horarios 
(idHorario, idFicha, idInstructor, idAmbiente, dias, jornadas, idTrimestre)
VALUES
(
UUID(),
JSON_ARRAY('F001'),
JSON_ARRAY('1003'),
JSON_ARRAY('Lab Sistemas'),
JSON_ARRAY('Lunes','Martes'),
JSON_ARRAY('Mañana'),
JSON_ARRAY('1')
);
