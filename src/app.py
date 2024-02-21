import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('credenciales.ini')
    api_key = config['gemini_ai']['API_KEY']

    chatbot = ChatBot(api_key=api_key)
    chatbot.iniciarConversacion()
    #chatbot.limpiar_conversacion

    print("Bienvenido al chatbot CLI de GDG Barranquilla. Escribe 'quit' para salir.")

    while True:
        user_input = input('Tú:')
        if user_input.lower() == 'quit':
            #print('Saliendo de chatbot CLI...')
            sys.exit('Saliendo de chatbot CLI...')
        
        try:
            response = chatbot.enviar_instruccion(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as error:
            print(f"Error: {error}")

main()


