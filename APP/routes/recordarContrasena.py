import flask_login
from flask import Flask, url_for, redirect, render_template, session, request
import mysql.connector
import yagmail


def conexion_db():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        database='bookshare'
    )
    cursor = mydb.cursor()


def recordarContrasena():
    return render_template('recordarContrasena.html')


def recordarContrasena_proceso():
    if not request.method == 'POST':
        return redirect(url_for('index'))

    conexion_db()
    correo = request.form['correo_recordar']

    if not correo:
        return "DATOS NO INGRESADOS"
    try:
        cursor.execute(
            "SELECT nombre_usuario, correo_usuario, contrasena_usuario FROM usuarios WHERE correo_usuario = %s", (correo, ))

        resultado = cursor.fetchone()

        if not resultado:
            print("CORREO NO ENCONTRADO. USUARIO NO ENCONTRADO")
            return "CORREO NO ENCONTRADO. USUARIO NO ENCONTRADO"

        if not correo == resultado[1]:
            print("CORREO INCORRECTO O NO ENCONTRADO")
            return "CORREO INCORRECTO O NO ENCONTRADO"

        print(f"DATOS INGREDASOS: \n{resultado}")

        nombreUsuario = resultado[0]
        contrasena = resultado[2]

        yag = yagmail.SMTP({
            'bookshare.attention@gmail.com': 'BookShare'
        }, 'ipal bhid isoq ysmc')

        contenido = f"""
        Estimado/a {nombreUsuario}:

        Hemos recibido una solicitud para recuperar tu contraseña en BookShare.
        A continuación, te proporcionamos tus credenciales de acceso:

        Tu contraseña temporal es: {contrasena}

        Por razones de seguridad, te recomendamos que cambies esta contraseña inmediatamente después de iniciar sesión en tu cuenta.

        Para hacerlo, sigue estos pasos:
        1. Ingresa a BookShare con tu contraseña temporal
        2. Ve a "Mi Perfil"
        3. Selecciona la opción "Cambiar Contraseña"
        4. Ingresa una nueva contraseña segura

        Si tú no solicitaste este cambio de contraseña, por favor contacta inmediatamente con nuestro equipo de soporte.

        ¿Necesitas ayuda adicional? Estamos aquí para asistirte.

        Saludos,
        El equipo de BookShare

        Nota: Este es un correo automático, por favor no respondas a este mensaje.
        """

        asunto = 'Recuperación de Contraseña - BookShare'

        yag.send(
            to=correo,
            subject='Recuperación de Contraseña - BookShare',
            contents=contenido
        )
        print("CORREO ENVIADO SATISFACTORIAMENTE")
        return redirect(url_for('iniciarSesion_ruta'))

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return "Error al enviar el correo"
    finally:
        if 'mydb' in globals():
            mydb.close()
