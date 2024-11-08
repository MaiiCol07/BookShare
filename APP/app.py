import flask_login
from flask import Flask, url_for, redirect, render_template, session, request, jsonify
from routes import registro, inicioSesion, inicio, recordarContrasena, perfil
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret_key'


def conexion_db():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        database='bookshare'
    )
    cursor = mydb.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def registro_ruta():
    return registro.registro()


@app.route('/registering', methods=['POST'])
def registro_proceso():
    return registro.registro_proceso()


@app.route('/login')
def inicioSesion_ruta():
    return inicioSesion.inicioSesion()


@app.route('/logining', methods=['POST'])
def inicioSesion_proceso():
    return inicioSesion.inicioSesion_proceso()


@app.route('/recoveryPass')
def recordarContrasena_ruta():
    return recordarContrasena.recordarContrasena()


@app.route('/recoveringPass', methods=['POST'])
def recordarContrasena_proceso():
    return recordarContrasena.recordarContrasena_proceso()


@app.route('/resultRecoveryPass/<resultado>')
def resultadoRecordarContrasena_ruta(resultado):
    return jsonify({"resultado": resultado}), 200, {'Content-Type': 'application/json'}

@app.route('/profile')
def perfil_ruta():
    return perfil.perfil()


@app.route('/home')
def inicio_ruta():
    return inicio.inicio()


@app.route('/logout')
def cerrarSesion():
    session.pop('usuarioLogueado', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
