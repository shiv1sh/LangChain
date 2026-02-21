from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv 
load_dotenv()

chat_template = ChatPromptTemplate([
    ('system','You are a helpful assistant that provides information'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []

with open('chathistory.txt') as f:
    for lines in f:
        chat_history.append(lines.strip())

model = ChatOpenAI(model = 'gpt-4.1-nano')
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'what is the status of my refund'})

print(prompt)

