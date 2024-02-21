# Chatbot CLI de GDG Barranquilla

Este proyecto es un chatbot de línea de comandos (CLI) desarrollado con Python y la API de Gemini AI de Google.

## Requisitos

* Python 3.7 o superior
* pipenv

## Instalación

1. Clonar el proyecto:

`````
git clone https://github.com/tu-usuario/chatbot-gdg-barranquilla.git
`````

2. Cambiar al directorio del proyecto:

`````
cd chatbot-gdg-barranquilla
`````

3. Crear un entorno virtual Python y activarlo:

`````
pipenv install
pipenv shell
`````


4. Instalar las dependencias:

`````
pipenv install -r requirements.txt
`````

5. (Opcional) Instalar Gradio para probar el chatbot en una interfaz web:

`````
pipenv install gradio
`````

## Ejecución

### Con credenciales de prueba:

`````
python src/app.py
`````

### Con tus propias credenciales:

1. Crea un archivo `credenciales.ini` en la raíz del proyecto.
2. Agrega la siguiente información al archivo:

`````
[gemini_ai]
API_KEY = <tu-api-key>
`````

3. Reemplaza `<tu-api-key>` con tu propia API key de Gemini AI.

4. Ejecuta el chatbot:

`````
python src/app.py
`````

## Uso

* Escribe un mensaje para el chatbot y presiona Enter.
* El chatbot te responderá con un mensaje generado por Gemini AI.
* Escribe "quit" para salir del chatbot.

## Pruebas

* Puedes probar el chatbot en una interfaz web con Gradio:

## Funcionalidades

* El chatbot puede responder a una amplia gama de preguntas y solicitudes.
* Puede generar diferentes tipos de contenido creativo, como poemas, código, guiones, piezas musicales, correos electrónicos, cartas, etc.
* Puede traducir idiomas.
* Puede responder preguntas de trivia.
* Puede ayudarte con tareas como escribir un resumen de un texto o generar un esquema para un ensayo.

## Limitaciones

* El chatbot aún está en desarrollo y puede cometer errores.
* La calidad de las respuestas del chatbot depende de la calidad de la entrada del usuario.
* El chatbot no puede realizar acciones en el mundo real.

## Próximos pasos

* Agregar más funcionalidades al chatbot.
* Mejorar la calidad de las respuestas del chatbot.
* Implementar un sistema de diálogo más natural.

## Contribuciones
* Puedes crear una nueva rama en el repositorio y enviar una solicitud de pull.

