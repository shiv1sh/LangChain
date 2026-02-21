from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv  

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')
chat_history = [SystemMessage(content="You are a helpful assistant that provides information about the latest advancements in AI research.")]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")