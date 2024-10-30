import flask_login
from flask import Flask, url_for, redirect, render_template, session, jsonify, flash
from routes import autenticador
import _mysql_connector

app = Flask(__name__)
app.secret_key = 'secret_key'

def conexion_db():
    global mydb, cursor
    mydb = _mysql_connector.connect(
        host = '127.0.0.1',
        user = 'root',
        database = 'bookshare'
    )
    cursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autenticador')
def autenticador_ruta():
    return autenticador.autenticador()

if __name__ == '__main__':
    app.run(debug=True, port=4000)