import flask_login
from flask import url_for, redirect, render_template, session, request
import mysql.connector

def conexion_db():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        database='bookshare'
    )
    cursor = mydb.cursor()

def registro():
    if 'usuarioLogueado' in session:
        return redirect(url_for('inicio_ruta'))
    else:
        return render_template('registro.html')

def registro_proceso():
    if request.method == "POST":
        conexion_db()

        nombre = request.form['nombre_registro']
        apellido = request.form['apellido_registro']
        correo = request.form['correo_registro']
        contrasena = request.form['contrasena_registro']

        if not nombre and not apellido and not correo and not contrasena:
            print("DATOS INCOMPLETOS")
            return 'DATOS INCOMPLETOS'
        
        cursor.execute("SELECT correo_usuario FROM usuarios WHERE correo_usuario = %s", (correo, ))

        resultadoConsulta = cursor.fetchone()

        if resultadoConsulta:
            print("EL USUARIO YA SE ENCUENTRA REGISTRADO")
            return redirect(url_for('inicioSesion_ruta'))
        
        cursor.execute("INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo_usuario, contrasena_usuario) VALUES (%s,%s,%s,%s)", (nombre, apellido, correo, contrasena))

        mydb.commit()

        print("REGISTRO EXITOSO")
        return redirect(url_for('inicioSesion_ruta'))
    else:
        return redirect(url_for('index'))