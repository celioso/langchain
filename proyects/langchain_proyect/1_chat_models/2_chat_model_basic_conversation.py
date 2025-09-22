from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv(dotenv_path="C:/Users/celio/OneDrive/Escritorio/programación/langchain/proyects/langchain_proyect/.env")

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")

"""messages = [
    SystemMessage(content="write an email"),
    HumanMessage(content="You can write an email to camilo@hotmail.com for a pending bill of 20 dollars."),
]

result = model.invoke(messages)
print(f"Answer from AI: {result.content}")"""