import json
import random
from difflib import get_close_matches

def carregar_intents(caminho):
    with open(caminho, "r") as arquivo:
        return json.load(arquivo)

def encontrar_resposta(texto_usuario, intents):
    for intent in intents["intents"]:
        if texto_usuario in intent["patterns"]:
            return random.choice(intent["responses"])
    return None

def chatbot():
    intents = carregar_intents("intents.json")
    print("Chatbot: Olá! Digite 'sair' para encerrar a conversa.")
    
    while True:
        texto_usuario = input("Você: ").strip()
        if texto_usuario.lower() == "sair":
            print("Chatbot: Tchau! Até a próxima.")
            break
        
        resposta = encontrar_resposta(texto_usuario, intents)
        if resposta:
            print(f"Chatbot: {resposta}")
        else:
            print("Chatbot: Desculpe, não entendi. Pode repetir?")

if __name__ == "__main__":
    chatbot()
