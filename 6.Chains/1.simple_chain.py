from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template = PromptTemplate(
    template = 'Generate 5 interesting fact about {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI(model='gpt-4')

output_parser = StrOutputParser()

chain = template | model | output_parser

response = chain.invoke({'topic': 'Cricket'})

chain.get_graph().print_ascii()  # Visualize the chain graph

print(response)