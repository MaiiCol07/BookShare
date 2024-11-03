import flask_login
from flask import Flask, url_for, redirect, render_template, session, request
import mysql.connector


def conexion_db():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        database='bookshare'
    )
    cursor = mydb.cursor()


def inicioSesion():
    if 'usuarioLogueado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('inicioSesion.html')


def inicioSesion_proceso():
    if request.method == "POST":
        conexion_db()

        correo = request.form['correo_login']
        contrasena = request.form['contrasena_login']

        if not correo or contrasena:
            print("DATOS NO INGRESADOS")
            return 'DATOS NO INGRESADOS'
        
        cursor.execute("SELECT id_usuario, contrasena_usuario FROM usuarios WHERE correo_usuario = %s", (correo, ))

        resultadoBusqueda = cursor.fetchone()

        if not resultadoBusqueda:
            print("USUARIO NO ENCONTRADO")
            return "USUARIO NO ENCONTRADOS"
        
        resultadoUsuario = resultadoBusqueda[0]
        resultadoContrasena = resultadoBusqueda[1]

        if not resultadoContrasena == contrasena:
            print("DATOS INCORRECTOS (Contraseña)")
            return "DATOS INCORRECTOS (Contraseña)"
        
        session['usuarioLogueado'] = int(resultadoUsuario)

        cursor.close()
        mydb.close()

        print(session[0])
        print("CONEXION CERRADA Y REDIRECCIONAMIENTO A 'HOME'")

        return redirect(url_for('inicio_ruta'))

    else:
        return redirect(url_for('inicioSesion_login'))