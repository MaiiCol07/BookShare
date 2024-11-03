import flask_login
from flask import url_for, redirect, render_template, session


def registro():
    if 'usuarioLogueado' in session:
        return redirect(url_for('inicio_ruta'))
    else:
        return render_template('registro.html')
