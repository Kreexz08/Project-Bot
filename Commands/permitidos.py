# commands/permitidos.py
from config import bot, USUARIOS_AUTORIZADOS

def handle_permitidos(message):
    if message.from_user.username != "Kreexz":
        bot.send_message(message.chat.id, "Usuario no autorizado para realizar esta acción.")
        return
    bot.send_message(message.chat.id, f"Usuarios autorizados: {', '.join(USUARIOS_AUTORIZADOS)}")
