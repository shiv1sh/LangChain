from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
prompt = PromptTemplate(
    template = 'Generate a summary of the topic \n {text}',
    input_variables = ['text']
)

model = ChatOpenAI(model = 'gpt-4.1-nano')

output_parser = StrOutputParser()

loader = TextLoader('cricket.txt')

docs = loader.load()

print(docs)

print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | output_parser

result = chain.invoke(docs[0].page_content)

print(result)