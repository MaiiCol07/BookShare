CREATE DATABASE bookshare;

USE bookshare;

CREATE TABLE universidades (
    id_universidad INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,
    nombre_universidad VARCHAR(50) NOT NULL,
    foto_universidad LONGBLOB NULL
);

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
    pNombre_usuario VARCHAR(50) NOT NULL,
    sNombre_usuario VARCHAR(50) NOT NULL,
    pApellido_usuario VARCHAR ( 50 ) NOT NULL,
    sApellido_usuario VARCHAR ( 50 ) NOT NULL,
    correo_usuario VARCHAR(200) NOT NULL UNIQUE,
    telefono_usuario VARCHAR(20) NULL UNIQUE,
    contrasena_usuario VARCHAR(200) NOT NULL,
    fk_universidad INT NOT NULL,
    descripcion_usuario VARCHAR ( 300 ) NULL,
    fechaNacimiento_usuario DATE NOT NULL,
    carrera_usuario VARCHAR ( 100 ) NULL,
    foto_usuario LONGBLOB NULL,
    CONSTRAINT fk_universidad
    FOREIGN KEY (fk_universidad) REFERENCES universidades(id_universidad)
);

CREATE TABLE editoriales (
    id_editorial INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    nombre_editorial VARCHAR(50) NOT NULL
);

CREATE TABLE autores (
	id_autor INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    nombre_autor VARCHAR(50) NOT NULL,
    apellido_autor VARCHAR(50) NOT NULL
);

CREATE TABLE generos (
	id_genero INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    nombre_genero VARCHAR(50) NOT NULL
);

CREATE TABLE estados_libros (
	id_estado INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    nombre_estado VARCHAR(50) NOT NULL
);

CREATE TABLE libros (
	id_libro INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    nombre_libro VARCHAR(200) NOT NULL,
    año_libro YEAR NULL,
    fk_usuarioPropietario INT NOT NULL,
    fk_genero INT NOT NULL,
    fk_autor INT NOT NULL,
    fk_editorial INT NOT NULL,
    fk_estado INT NOT NULL,
    descripcion_libro VARCHAR(300) NULL,
    foto_libro LONGBLOB NULL,
    CONSTRAINT fk_usuario
    FOREIGN KEY (fk_usuarioPropietario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_genero
    FOREIGN KEY (fk_genero) REFERENCES generos(id_genero),
    CONSTRAINT fk_autor
    FOREIGN KEY (fk_autor) REFERENCES autores(id_autor),
    CONSTRAINT fk_editorial
    FOREIGN KEY (fk_editorial) REFERENCES editoriales(id_editorial),
    CONSTRAINT fk_estado
    FOREIGN KEY (fk_estado) REFERENCES estados_libros(id_estado)
);

CREATE TABLE intercambios (
	id_intercambio INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    fk_usuarioRemitente INT NOT NULL,
    fk_usuarioReceptor INT NOT NULL,
    fk_libro INT NOT NULL,
    fechaHora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado_intercambio ENUM('Realizado','Pendiente','Rechazado'),
    CONSTRAINT fk_usuarioRemitente
    FOREIGN KEY (fk_usuarioRemitente) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_usuarioReceptor
    FOREIGN KEY (fk_usuarioReceptor) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_libro
    FOREIGN KEY (fk_libro) REFERENCES libros(id_libro)
);

CREATE TABLE mensajes (
	id_mensaje INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    texto_mensaje LONGTEXT NOT NULL,
    foto_mensaje LONGBLOB NULL,
    fk_usuarioRemitente INT NOT NULL,
    fk_usuarioReceptor INT NOT NULL,
    CONSTRAINT fk_usuarioRemitenteMsg
    FOREIGN KEY (fk_usuarioRemitente) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_usuarioReceptorMsg
    FOREIGN KEY (fk_usuarioReceptor) REFERENCES usuarios(id_usuario)
);

CREATE TABLE calificaciones (
	id_calificacion INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    fk_usuarioCalificador INT NOT NULL,
    fk_usuarioCalificado INT NOT NULL,
    fk_intercambio INT NOT NULL,
    calificacion INT(1) NOT NULL,
    descripcion_calificacion VARCHAR(500) NULL,
    CONSTRAINT fk_usuarioCalificador
    FOREIGN KEY (fk_usuarioCalificador) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_usuarioCalificado
    FOREIGN KEY (fk_usuarioCalificado) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_intercambio
    FOREIGN KEY (fk_intercambio) REFERENCES intercambios(id_intercambio),
    CONSTRAINT calificacion_unica UNIQUE (fk_usuarioCalificador, fk_usuarioCalificado, fk_intercambio)
);
