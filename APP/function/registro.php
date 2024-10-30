<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    include "database.php";

    $pNombre = $_POST['pNombre_registro'];
    if ($_POST['sNombre_registro']) {
        $sNombre = $_POST['sNombre_registro'];
    } else {
        $sNombre = "";
    }
    $pApellido = $_POST['pApellido_registro'];
    $sApellido = $_POST['sApellido_registro'];
    $correo = $_POST['correo_registro'];
    $contrasena = $_POST['contrasena_registro'];
    $vContrasena = $_POST['vContrasena_registro'];

    if ($contrasena == $vContrasena) {

        $query = "SELECT correo_usuario FROM usuarios WHERE correo_usuario = '$correo'";

        function verificarCorreo($conexion, $query): bool
        {
            if (mysqli_query(mysql: $conexion, query: $query)->num_rows > 0) {
                echo 'Se encontró un correo ya registrado en la base de datos.';
                return false;
            } else {
                echo 'No se encontró algún correo en la base de datos. Puede continuar.';
                return true;
            }
        }

        if (verificarCorreo(conexion: $conexion, query: $query)) {
            $query_insert = "INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo_usuario) VALUES ('$pNombre','$pApellido', '$correo')";

            if (mysqli_query(mysql: $conexion, query: $query_insert)) {
                echo 'Los datos fuero ingresados correctamente en la base de datos';
                header(header: "Location: inicio.html");
                exit;
            } else {
                echo 'Error en la insersión de datos: ' . mysqli_error(mysql: $conexion);
            }
        }
    } else {
        echo 'Las contraseñas ingresadas son difententes';
    }
}
