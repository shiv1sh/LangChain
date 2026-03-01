from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a Joke on the topic \n {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI(model = 'gpt-4.1-nano')

output_parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, output_parser)

result = chain.invoke({'topic' : 'Langchain'})

print(result)
