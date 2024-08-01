# commands/consulta.py
from config import bot, USUARIOS_AUTORIZADOS
import requests
import json

def handle_consulta(message):
    if message.from_user.username not in USUARIOS_AUTORIZADOS:
        bot.send_message(message.chat.id, "Usuario no autorizado. Escribeme si quieres más información @Kreexz.")
        return
    
    comando = message.text.split()[0]
    numero_completo = message.text.split()[1] if len(message.text.split()) > 1 else None

    if comando != '/consulta':
        bot.send_message(message.chat.id, "Comando no válido. Ingrese /consulta seguido del número de teléfono (con el código de país 506).")
        return
    elif not numero_completo or not numero_completo.startswith('506') or len(numero_completo) != 11:
        bot.send_message(message.chat.id, "Debe ingresar un número de teléfono válido después del comando /kolbi en el formato 506XXXXXXXX.")
        return

    numero = numero_completo[3:]  # Extrae el número sin el código de país

    try:
        headers = {'Content-Type': 'application/json'}
        data = {'telefono': numero, 'key': 'AQUI_VA_TU_API_KEY_PARA_CONSULTAR'}
        data_json = json.dumps(data)

        respuesta = requests.post('AQUI_VA_LA_API', headers=headers, data=data_json)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f"Error al conectar con la API: {e}")
        return

    try:
        respuesta_json = respuesta.json()
    except json.JSONDecodeError:
        bot.send_message(message.chat.id, "Error al decodificar la respuesta de la API. Intente nuevamente más tarde.")
        return

    if respuesta_json['status'] == 200:
        detalle_servicio = respuesta_json['listaObjetos'][0]['detalleServicio']
        nombre_cliente = detalle_servicio['nombreCliente']
        cedula_cliente = detalle_servicio['cedulaCliente']
        telefono = detalle_servicio['telefono']
        estado_linea = detalle_servicio['estado']
        nombre_producto = detalle_servicio['nombreProducto']

        respuesta_texto = f"""
Nombre: {nombre_cliente}
Cédula: {cedula_cliente}
Número: {telefono}
Estado de la línea: {estado_linea}
Producto: {nombre_producto}
        """
        bot.send_message(message.chat.id, respuesta_texto)
    else:
        bot.send_message(message.chat.id, f"Error al consultar la información: {respuesta_json.get('message', 'Intente nuevamente más tarde.')}")