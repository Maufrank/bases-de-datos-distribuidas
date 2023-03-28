from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template, Request
from firebase import firebase
from datetime import datetime

app = Blueprint('rutas', __name__, url_prefix='/')


@app.get('/')
def main():
    return render_template('add_tutor.html')

@app.route('/bases/sucursales')
def bases_sucursales():
    return render_template('find_permiso.html')

@app.route('/esclavo')
def esclavo():
    return render_template('add_alumno.html')

@app.route('/alumnos')
def ver_alumnos():
    return render_template('find_alumnos.html')