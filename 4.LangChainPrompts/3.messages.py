from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [SystemMessage(content="You are a helpful assistant that provides information about the latest advancements in AI research."),
            HumanMessage(content = "What are the latest advancements in AI research?")]

model = ChatOpenAI(model = 'gpt-4.1-nano')
user_input = HumanMessage(content = input("You: "))
messages.append(user_input)
response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)