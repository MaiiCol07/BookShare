import flask_login
from flask import url_for, redirect, render_template, session

def inicio():
    if 'usuarioLogueado' in session:
        return render_template('inicio.html')
    else:
        return redirect(url_for('inicioSesion_ruta'))
