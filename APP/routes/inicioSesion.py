import flask_login
from flask import url_for, redirect, render_template, session

def inicioSesion():
    if 'usuarioLogueado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('inicioSesion.html')
