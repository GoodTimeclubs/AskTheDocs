import os
import requests
from dotenv import load_dotenv

#read .env file
load_dotenv()

testPrompt = "Hello, Sir :)"

#get .env values
model = os.getenv("OLLAMA_CHAT_MODEL") #ToDo dynamicly pull moddel list and throw error when list is empty
ollamaUrl = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

#start request to model
payload = {
    "model": model,
    "prompt":testPrompt,
    "stream":False,
    "options" : {"temperature": 0}
}
r = requests.post(f"{ollamaUrl}/api/generate",json=payload, timeout=500)

#print response and metrics
print(r.json()["response"])
print(f"Completed in {r.json()["total_duration"]/1000000000} seconds.")
print(f"With {r.json()["prompt_eval_count"]} input and {r.json()["eval_count"]} output tokens.")
print(f"With a Cache hit rate of { round((r.json()["prompt_eval_cached_count"]*100)/ r.json()["prompt_eval_count"],2)}%")