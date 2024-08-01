from app import app
import os
import subprocess
import threading
import time

# Variable global para almacenar el proceso del bot
bot_process = None

def start_bot():
    global bot_process
    bot_process = subprocess.Popen(["python", "bot.py"])



if __name__ == '__main__':
    

    
    # Ejecutar la aplicación Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
