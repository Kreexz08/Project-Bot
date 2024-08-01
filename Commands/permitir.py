# commands/permitir.py
from config import bot, USUARIOS_AUTORIZADOS

def handle_permitir(message):
    if message.from_user.username != "Kreexz":
        bot.send_message(message.chat.id, "Usuario no autorizado para realizar esta acción.")
        return

    usuario = message.text.split()[1] if len(message.text.split()) > 1 else None
    if usuario:
        USUARIOS_AUTORIZADOS.add(usuario)
        bot.send_message(message.chat.id, f"Usuario @{usuario} autorizado para utilizar el bot.")
    else:
        bot.send_message(message.chat.id, "Debe ingresar el nombre de usuario después del comando /permitir.")
