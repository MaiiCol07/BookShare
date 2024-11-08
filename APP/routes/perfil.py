import flask_login
from flask import url_for, redirect, render_template, session, request
import mysql.connector, base64
from datetime import datetime


def conexion_db():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        database='bookshare'
    )
    cursor = mydb.cursor()


def perfil():
    if not 'usuarioLogueado' in session:
        return redirect(url_for('inicioSesion_ruta'))

    conexion_db()

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s",
                   (session['usuarioLogueado'], ))
    busqueda = cursor.fetchone()
    
    fecha_actual = datetime.now()
    if busqueda[7]:
        fechaNacimiento = datetime.strptime(busqueda[7], "%Y-%m-%d")
        edad = fecha_actual.year - fechaNacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fechaNacimiento.month, fechaNacimiento.day))
    else:
        edad = None
    
    foto = None
    if busqueda[8]:
        foto = base64.b64encode(busqueda[8]).decode('utf-8')

    datos_usuario = {
        "nombre": busqueda[1],
        "apellido": busqueda[2],
        "correo": busqueda[3],
        "telefono": busqueda[4],
        "descripcion": busqueda[6],
        "edad": edad,
        "foto": foto
    }

    return render_template('perfil.html', usuario = datos_usuario)
