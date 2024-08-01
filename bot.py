# bot.py
from config import bot
from Commands.start import handle_start
from Commands.permitir import handle_permitir
from Commands.denegar import handle_denegar
from Commands.permitidos import handle_permitidos
from Commands.comandos import handle_comandos
from Commands.consulta import handle_consulta
from Commands.sacar import handle_sacar
from Commands.agregar import handle_agregar

bot.message_handler(commands=['start'])(handle_start)
bot.message_handler(commands=['permitir'])(handle_permitir)
bot.message_handler(commands=['denegar'])(handle_denegar)
bot.message_handler(commands=['permitidos'])(handle_permitidos)
bot.message_handler(commands=['comandos'])(handle_comandos)
bot.message_handler(commands=['consulta'])(handle_consulta)
bot.message_handler(commands=['sacar'])(handle_sacar)
bot.message_handler(commands=['agregar'])(handle_agregar)

if __name__ == '__main__':
    bot.polling(none_stop=True)
