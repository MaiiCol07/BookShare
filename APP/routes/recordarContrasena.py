import flask_login
import smtplib
from flask import Flask, url_for, redirect, render_template, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        return jsonify({"resultado": "error", "mensaje": "Método no permitido"})

    conexion_db()
    correo = request.form['correo_recordar']

    if not correo:
        return jsonify({"resultado": "error", "mensaje": "Correo no proporcionado"})

    try:
        cursor.execute(
            "SELECT nombre_usuario, correo_usuario, contrasena_usuario FROM usuarios WHERE correo_usuario = %s", (correo, ))

        resultado = cursor.fetchone()

        if not resultado:
            print("CORREO NO ENCONTRADO. USUARIO NO ENCONTRADO")
            return jsonify({"resultado": "error", "mensaje": "Correo no encontrado"})

        print(f"DATOS INGREDASOS: \n{resultado}")

        nombreUsuario = resultado[0]
        contrasena = resultado[2]

        emisor = "bookshare.attention@gmail.com"
        contrasenaEmisor = "ipal bhid isoq ysmc"
        contenido = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    color: #2C7DB4;
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .password {{
                    background: #f5f5f5;
                    padding: 10px;
                    margin: 15px 0;
                    border-radius: 4px;
                }}
                .steps {{
                    margin: 15px 0;
                }}
                .footer {{
                    font-size: 12px;
                    color: #666;
                    border-top: 1px solid #eee;
                    margin-top: 30px;
                    padding-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                Estimado/a {nombreUsuario}:
            </div>

            <p>Hemos recibido una solicitud para recuperar tu contraseña en BookShare.</p>
            <p>A continuación, te proporcionamos tus credenciales de acceso:</p>

            <div class="password">
                <strong>Tu contraseña actual es:</strong> {contrasena}
            </div>

            <p><strong>Por razones de seguridad</strong>, te recomendamos que cambies esta contraseña inmediatamente después de iniciar sesión en tu cuenta.</p>

            <div class="steps">
                <p>Para hacerlo, sigue estos pasos:</p>
                <ol>
                    <li>Ingresa a BookShare con tu contraseña temporal</li>
                    <li>Ve a "Mi Perfil"</li>
                    <li>Selecciona la opción "Cambiar Contraseña"</li>
                    <li>Ingresa una nueva contraseña segura</li>
                </ol>
            </div>

            <p>Si tú no solicitaste este cambio de contraseña, por favor contacta inmediatamente con nuestro equipo de soporte.</p>

            <p>¿Necesitas ayuda adicional? Estamos aquí para asistirte.</p>

            <p>Saludos,<br>
            El equipo de BookShare</p>

            <div class="footer">
                <em>Nota: Este es un correo automático, por favor no respondas a este mensaje. Si necesitas asistencia, abre una nueva conversación con nuestro equipo de soporte.</em>
            </div>
        </body>
        </html>
        """
        asunto = 'Recuperación de Contraseña - BookShare'

        mensaje = MIMEMultipart()
        mensaje['from'] = emisor
        mensaje['to'] = correo
        mensaje['subject'] = asunto

        mensaje.attach(MIMEText(contenido, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(emisor, contrasenaEmisor)
            texto = mensaje.as_string()
            servidor.sendmail(emisor, correo, texto)

        print("CORREO ENVIADO SATISFACTORIAMENTE")
        return jsonify({"resultado": "success", "mensaje": "Correo enviado exitosamente"})
    except:
        print(f"Error al enviar el correo")
        return jsonify({"resultado": "error", "mensaje": "Error al enviar el correo"})
    finally:
        if 'mydb' in globals():
            mydb.close()
