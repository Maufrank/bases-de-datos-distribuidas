import os
from flask import Flask, send_from_directory, session, request, redirect
# from dotenv import load_dotenv


from features.db import conexionDB as conexion
from features.rutes_views import rutas as vistas



app = Flask(__name__)
app.secret_key = 'treecko_secret_key'


app.register_blueprint(conexion.app)
app.register_blueprint(vistas.app)


if __name__ == "__main__":
    app.run()

    

