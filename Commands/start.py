# commands/start.py
from config import bot, USUARIOS_AUTORIZADOS

def handle_start(message):
    usuario = message.from_user.username
    if usuario in USUARIOS_AUTORIZADOS:
        bot.send_message(message.chat.id,
                         "Bienvenido al bot.\n\n"
                         "Utiliza el comando /comandos para conocer todos los comandos disponibles.")
    else:
        bot.send_message(message.chat.id, "Usuario no autorizado. Para obtener más información, contacta a @Kreexz.")
