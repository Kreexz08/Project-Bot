import json
import os
import telebot


TOKEN = "AQUI_VA_TU_TOKEN_DE_TELEGRAM"
bot = telebot.TeleBot(TOKEN)

USUARIOS_ARCHIVO = 'usuarios.json'

def cargar_usuarios():
    if os.path.exists(USUARIOS_ARCHIVO):
        with open(USUARIOS_ARCHIVO, 'r') as f:
            return set(json.load(f))
    return set()

def guardar_usuarios(usuarios):
    with open(USUARIOS_ARCHIVO, 'w') as f:
        json.dump(list(usuarios), f)

# Inicializar la lista de usuarios al iniciar la aplicación
USUARIOS_AUTORIZADOS = cargar_usuarios()

def agregar_usuario(usuario):
    USUARIOS_AUTORIZADOS.add(usuario)
    guardar_usuarios(USUARIOS_AUTORIZADOS)

def eliminar_usuario(usuario):
    USUARIOS_AUTORIZADOS.discard(usuario)
    guardar_usuarios(USUARIOS_AUTORIZADOS)
