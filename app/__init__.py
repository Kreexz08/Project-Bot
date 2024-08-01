import os
from flask import Flask

app = Flask(__name__)

# Obtén la clave secreta de las variables de entorno
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Cambia 'default_secret_key' por una clave segura o deja una predeterminada para desarrollo

# Importa tus rutas aquí
from app import routes