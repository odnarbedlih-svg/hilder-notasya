-- Datos iniciales para NOTASYA (Universidad de Manizales)
INSERT INTO estudiantes (nombre, telefono, correo) VALUES ('Hildebrando Tangarife Cardona', '3101234567', 'htangarife@umanizales.edu.co');
INSERT INTO estudiantes (nombre, telefono, correo) VALUES ('Hildebrando Tangarife Cardona', '3209876543', 'htangarife@umanizales.edu.co');
INSERT INTO estudiantes (nombre, telefono, correo) VALUES ('Laura Valentina Gómez', '3158889900', 'lgomez@umanizales.edu.co');

INSERT INTO profesores (nombre, tipo_identificacion, numero_identificacion, especialidad) VALUES ('Dr. Jorge Luis Aguirre', 'CC', '1053800900', 'Diseño y Arquitectura de Software');
INSERT INTO profesores (nombre, tipo_identificacion, numero_identificacion, especialidad) VALUES ('Dra. Claudia Ortiz', 'CC', '1024500600', 'Bases de Datos y Cloud Computing');

INSERT INTO cursos (nombre, estudiante_id, profesor_id, calificacion) VALUES ('Diseño de Sistemas de Información', 1, 1, 4.8);
INSERT INTO cursos (nombre, estudiante_id, profesor_id, calificacion) VALUES ('Diseño de Sistemas de Información', 2, 1, 5.0);
INSERT INTO cursos (nombre, estudiante_id, profesor_id, calificacion) VALUES ('Bases de Datos Avanzadas', 3, 2, 4.2);
