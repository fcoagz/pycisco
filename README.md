# pycisco
Es un proyecto personal desarrollado para comunicarse con una inteligencia artificial. `pycisco` es un simple bot de Telegram que te permite comunicarte gratis (por el momento) con algunos modelos de lenguaje que ofrece actualmente. pycisco entiende el mensaje que envía y utiliza herramientas de lenguaje natural para analizar el sentimiento del mensaje y responder de acuerdo a lo que dice el usuario.

## Funcionamiento
1. Clona el repositorio de GitHub:
```sh
git clone https://github.com/fcoagz/pycisco
```
2. Instale los paquetes de Python necesarios desde `requirements.txt`:
```sh
pip install -r requirements.txt
```
3. Agregue el token del bot de Telegram en `src/config_bot.py`. Variable `token`
4. Ejecutar script:
```sh
python main.py
```

## Detalles
`pycisco` tiene la capacidad de limitar el número de solicitudes a 15 por minuto para evitar bloquear el código.

Entre las funciones que provee el bot, tenemos:

1. Permite iniciar la conversación con el bot y comenzar a hacer uso de sus funciones.
```
/start
```
2. Muestra los comandos disponibles para ejecutar por el bot.
```
/help
```
3. Permite obtener un detalle de los Modelos de Lenguaje que ofrece el bot.
```
/model
```
4. Configura la inteligencia artificial y el modelo de lenguaje que deseas utilizar. `/model` Obtendra los detalles.
```
/config <Ai> <Modelo>
```

## Agradecimientos
Muchas gracias a [xtekky](https://github.com/xtekky), por crear una herramienta tan poderosa.