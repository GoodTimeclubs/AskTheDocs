import os
import requests
from dotenv import load_dotenv

def embedChunks(input):
    #read .env file
    load_dotenv()

    #get .env values
    model = os.getenv("OLLAMA_EMB_MODEL") #ToDo dynamicly pull moddel list and throw error when list is empty
    ollamaUrl = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    #start request to model
    payload = {
        "model": model,
        "input":input,
        "options" : {"temperature": 0}
    }
    r = requests.post(f"{ollamaUrl}/api/embed",json=payload, timeout=500)

    return(r.json()["embeddings"])
