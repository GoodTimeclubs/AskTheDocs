This chatbot is based on a RAG pipeline to provide accurate answers to questions about documents without hallucinating. The project includes a Docker Compose setup that can be connected to a locally hosted AI via an Ollama server.

**This project is developed without using any AI-generated code or configuration files.**




The AI for Ollama can be installed with the following command:

`ollama pull gemma4:e2b`



Set up the embedding:

`ollama pull bge-m3` 

German example of the AI answering based on a test document:

Conversation:
<img width="1005" height="96" alt="image" src="https://github.com/user-attachments/assets/d0b6ce18-4d60-4c5b-8d1c-234919dff3e8" />

Source file (one of 10 files with only the relevant part given to the AI):
<img width="789" height="994" alt="image" src="https://github.com/user-attachments/assets/6c1d51e9-7dfe-4ae6-92de-e073ceea9904" />

