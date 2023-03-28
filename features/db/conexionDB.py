from flask import Blueprint, render_template, request, json, redirect, session, jsonify
# import request
# from firebase_admin import bd
from firebase import firebase
# from flask_wtf import CSRFProtect
app = Blueprint('conexion', __name__, url_prefix='/conexion')

bd = firebase.FirebaseApplication(
    "https://basededatosdistribuida-24979-default-rtdb.firebaseio.com/", None)

@app.route('/registrar/sucursal', methods=['POST'])
def registrar_sucursal():
    sucursal = {
        "nombre": request.form['sucursal'],
        "url": request.form['url'],
        "usuario": request.form['usuario'],
        "password": request.form['pass'],
    }

    bd.post('/sucursales', sucursal)
    return redirect('/')

@app.route('/bases')
def get_sucursales():
    sucursales = bd.get('/sucursales', '')
    data = []
    for sucursal in sucursales:
        datos = sucursales[sucursal]
        data.append(datos)
        
    return jsonify({"datos": data})

@app.route('/get/alumnos')
def get_alumnos():
    sucursales = bd.get('/sucursales', '')
    data = []
    for sucursal in sucursales:
        datos = sucursales[sucursal]
        url = datos['url']
        
        base = firebase.FirebaseApplication(url, None)
        datos = base.get('/alumnos', '')
        for dato in datos:
            alumno = datos[dato]
            print(alumno)
            data.append(alumno)
        
    return jsonify({"datos": data})
    