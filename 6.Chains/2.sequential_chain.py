from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a report for the following topic {topic}',
    input = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following report {report}',
    input = ['report']
)

model = ChatOpenAI(model = 'gpt-4.1-nano')

output_parser = StrOutputParser()

chain = prompt1 | model | output_parser | prompt2 | model | output_parser

result = chain.invoke({'topic': 'The impact of AI on society'})

print(result)