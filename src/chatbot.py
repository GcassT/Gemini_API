import google.generativeai as genai

class GeniAIException(Exception):
    """GenAi Excepcion base class"""

class ChatBot:
    """El chat solo puede tener un usuario al tiempo"""
    CHATBOT_NAME = 'GDG Gemini API'

    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key=api_key)
        self.model = self.genai.GenerativeModel('gemini-pro')
        self.conversacion = None
        self._historial_conversacion = []

        self.cargar_conversciones()

    def enviar_instruccion(self, instruccion, temperature=0.1):
        if temperature < 0 or temperature > 1:
            raise GeniAIException('¿Temperature debe estar entre 0 y 1!')
        
        if not instruccion:
            raise GeniAIException('¡La instrucción no puede ir vacía!')
        
        try:
            response = self.conversacion.send_message(
                content=instruccion,
                generation_config=self._generar_config(temperature),
            )
            response.resolve()
            return f'{response.text}\n' + '---' * 20
        except Exception as error:
            raise GeniAIException(error.message)
    
    @property
    def historial(self):
        historial_conversacion = [
            {'role': message.role, 'text': message.parts[0].text} for message in self.conversacion.historial
        ]
        
        return historial_conversacion
    
    def limpiar_conversacion(self):
        self.conversacion = self.model.start_chat(history=[])
    
    def iniciarConversacion(self):
        self.conversacion = self.model.start_chat(history=self._historial_conversacion)

    def _generar_config(self, temperature):
        return genai.types.GenerationConfig(
            temperature=temperature
        )

    def _construir_mensaje(self, text, role='user'):
        return {
            'role': role,
            'parts': [text]
        }

    def cargar_conversciones(self, historial_conversacion=None):
        if isinstance(historial_conversacion, list):
            self._historial_conversacion = historial_conversacion
        else:
            self._historial_conversacion = [
                self._construir_mensaje('Puedes decirme cuanto los primeros 20 decimales del número pi.'),
                self._construir_mensaje('{"text": Clar´, los primeros 20 decimales del número pi son: }','model')
            ]