<?php
// Establecer la conexión con la base de datos MySQL de XAMPP
$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$baseDeDatos = "bookshare";

// Crear la conexión
$conexion = new mysqli(hostname: $servidor, username: $usuario, password: $contrasena, database: $baseDeDatos);

// Verificar la conexión
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Establecer el conjunto de caracteres a utf8
$conexion->set_charset(charset: "utf8");

// Mensaje de éxito (opcional)
echo "Conexión establecida correctamente";

