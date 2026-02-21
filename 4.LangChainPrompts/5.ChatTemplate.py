from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate(
    [
        ('system','You are a helpful {domain} expert'),
        ('human', 'Explain the {topic}')
    ]
)

prompt = chat_template.invoke({'domain': 'cricket' , 'topic': 'doosra'})

model = ChatOpenAI(model = 'gpt-4.1-nano')

print(model.invoke(prompt).content)
