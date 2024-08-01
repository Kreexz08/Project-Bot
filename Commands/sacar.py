# commands/sacar.py
from config import bot

def handle_sacar(message):
    if message.from_user.username != "Kreexz":
        bot.send_message(message.chat.id, "Usuario no autorizado para realizar esta acción.")
        return
    usuario = message.text.split()[1] if len(message.text.split()) > 1 else None
    if usuario:
        bot.kick_chat_member(message.chat.id, usuario)
        bot.send_message(message.chat.id, f"Usuario {usuario} eliminado del grupo.")
    else:
        bot.send_message(message.chat.id, "Debe ingresar el nombre de usuario después del comando /sacar.")
