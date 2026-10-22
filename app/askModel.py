import os
import requests
from dotenv import load_dotenv
from findCloseEmbed import findCloseEmbed



def askModel(question):
    #read .env file
    load_dotenv()

    details = findCloseEmbed(question)

    #get .env values
    model = os.getenv("OLLAMA_CHAT_MODEL") #ToDo dynamicly pull moddel list and throw error when list is empty
    ollamaUrl = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    sysPrompt = "You are a chatbot that answers questions about documentations.\nBase your answers only of the 5 information blocks given below, which include the headlines for the block.\nIf a information is not included, tell the user, that this question is not part of yout intended scope.\n Only include the latest information about the given topic in your response. \nCheck your answer for spelling mistakes before replying. \nWrite the answer in plain text without Markdown formating.\n The information for the current task is:"


    system = sysPrompt +details

    #start request to model
    payload = {
        "model": model,
        "prompt":question,
        "system":system,
        "stream":False,
        "options" : {"temperature": 0}
    }
    r = requests.post(f"{ollamaUrl}/api/generate",json=payload, timeout=500)
    return r.json()["response"]