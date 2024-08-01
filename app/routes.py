import os
import subprocess
from app import app
from flask import render_template, request, redirect, url_for, flash, session
from config import USUARIOS_AUTORIZADOS, agregar_usuario, eliminar_usuario

# Variable global para almacenar el proceso del bot
bot_process = None

@app.route('/')
def index():
    mensaje = session.get('mensaje')
    tipo_mensaje = session.get('tipo_mensaje', 'info')
    session.pop('mensaje', None)
    session.pop('tipo_mensaje', None)
    return render_template('index.html', mensaje=mensaje, tipo_mensaje=tipo_mensaje)

@app.route('/start-bot')
def start_bot():
    global bot_process
    if bot_process is None or bot_process.poll() is not None:
        # Iniciar el bot solo si no está en ejecución
        bot_process = subprocess.Popen(["python", "bot.py"])
        session['mensaje'] = "Se ha iniciado correctamente el bot."
        session['tipo_mensaje'] = 'success'
    else:
        # Si el bot ya está en ejecución
        session['mensaje'] = "El bot ya está iniciado."
        session['tipo_mensaje'] = 'info'
    return redirect(url_for('index'))


@app.route('/stop-bot')
def stop_bot():
    global bot_process
    if bot_process is not None:
        bot_process.terminate()
        bot_process.wait()
        bot_process = None
        session['mensaje'] = "Se ha detenido correctamente el bot."
        session['tipo_mensaje'] = 'error'
    else:
        session['mensaje'] = "El bot ya está apagado."
        session['tipo_mensaje'] = 'info'
    return redirect(url_for('index'))

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    global bot_process

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        action = request.form.get('action')

        if not usuario:
            flash("Debe ingresar un nombre de usuario.", 'info')
            return redirect(url_for('usuarios'))

        if action == 'add':
            if usuario in USUARIOS_AUTORIZADOS:
                flash("El usuario ya está en la lista.", 'info')
            else:
                agregar_usuario(usuario)
                flash("Usuario agregado correctamente.", 'success')
                # Detener y reiniciar el bot después de agregar un usuario
                if bot_process:
                    bot_process.terminate()
                    bot_process.wait()  # Esperar a que el proceso se termine completamente
                bot_process = subprocess.Popen(["python", "bot.py"])
        elif action == 'remove':
            if usuario in USUARIOS_AUTORIZADOS:
                eliminar_usuario(usuario)
                flash("Usuario eliminado correctamente.", 'error')
                # Detener y reiniciar el bot después de eliminar un usuario
                if bot_process:
                    bot_process.terminate()
                    bot_process.wait()  # Esperar a que el proceso se termine completamente
                bot_process = subprocess.Popen(["python", "bot.py"])
        else:
            flash("Acción no válida.", 'info')
        
        return redirect(url_for('usuarios'))

    return render_template('usuarios.html', usuarios=USUARIOS_AUTORIZADOS)
