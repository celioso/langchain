import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Cargar variables desde el .env que está en otra carpeta
load_dotenv(dotenv_path="C:/Users/celio/OneDrive/Escritorio/programación/langchain/proyects/langchain_proyect/.env")

# (opcional) verificar que la API key se haya cargado
# print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Usar el modelo
model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)

result = model.invoke("What is 81 minus 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)