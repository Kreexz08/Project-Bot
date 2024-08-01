# commands/comandos.py
from config import bot, USUARIOS_AUTORIZADOS


def handle_comandos(message):
    bot.reply_to(message, "Estos son los comandos disponibles para los permitidos o autorizados:\n/start - Iniciar\n/comandos - Comandos\n/agregar - Meter gente al grupo\n/sacar - Eliminar gente del grupo\n/consulta - este comando se usa seguido de un numero kolbi de costa rica para consultar su informacion\n\n"
                 "Tambien hay unos comandos para el dueño del bot como lo son: \n/permitir - Permite a alguien usar el bot\n/denegar - Deniega a alguien usar el bot\n/usuarios - Muestra los usuarios permitidos\n\n")
