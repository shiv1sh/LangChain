from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate a summary of the topic \n {text}',
    input_variables = ['text']
)  

model = ChatOpenAI(model = 'gpt-4.1-nano')

output_parser = StrOutputParser()

loader = PyPDFLoader('cricket_rules.pdf')

docs = loader.load()

chain = prompt | model | output_parser

result = chain.invoke(docs[0].page_content)