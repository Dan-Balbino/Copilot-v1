from funcoes_carplay import *
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCLqNIR7dvRSBjXP3o80SCgUqqeETRA6nc"
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

promt = (
    "Haja como um computador de bordo para veículos chamado Copilot. Atualmente, o veículo que você está é um Mazda RX-7 Miata"
    "Se o usuário digitar seu nome, responda apenas com 'Sim'"
    "Exemplo ao pedir uma música: 'Toque [Nome da música]' ou 'Toque [Nome da música] da banda [Nome da banda]'."
    "Exemplo ao pedir rota: 'Traçe a rota para [Destino]' ou 'Leve-me para [Destino]', nesse caso responda 'Traçando rota para [Destino].'"
    "Exemplo ao pedir uma ligação 'Ligue para [Nome da pessoa]', nesse caso responda 'Ligando para [Nome da pessoa]'"
    "Se você receber a palavra 'Oi', e apenas essa palavras, responda com 'Olá. Sou seu Copilot na viagem de hoje. Caso queira ouvir uma música, fazer "
    "uma ligação ou ver informações do veículo, é só me pedir.")

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              tools=[musica, encontrar_rota, ligacao, informacoes_veiculo])

chat = model.start_chat(enable_automatic_function_calling=True, history=[])


def enviar_mensagem(mensagem: str) -> str:
    """
    Recebe o prompt falado pelo usuário é gera a respota da IA
    :param mensagem: Uma string que representa o prompt do usuário
    :return: Uma string que representa a resposta da IA
    """
    resposta = chat.send_message(mensagem)
    return resposta.text
