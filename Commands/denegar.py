# commands/denegar.py
from config import bot, USUARIOS_AUTORIZADOS

def handle_denegar(message):
    if message.from_user.username != "Kreexz":
        bot.send_message(message.chat.id, "Usuario no autorizado para realizar esta acción.")
        return

    usuario = message.text.split()[1] if len(message.text.split()) > 1 else None
    if usuario:
        USUARIOS_AUTORIZADOS.discard(usuario)
        bot.send_message(message.chat.id, f"Usuario @{usuario} denegado para utilizar el bot.")
    else:
        bot.send_message(message.chat.id, "Debe ingresar el nombre de usuario después del comando /denegar.")
