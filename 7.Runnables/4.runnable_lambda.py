from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def function_to_calculate_length_of_joke(joke: str):
    return len(joke.split())

prompt = PromptTemplate(
    template = 'Generate a Joke on the topic \n {topic}',
    input_variables = ['topic']
)

output_parser = StrOutputParser()

model = ChatOpenAI(model = 'gpt-4.1-nano')

joke_generation_chain = RunnableSequence(prompt, model, output_parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'joke_length' : RunnableLambda(function_to_calculate_length_of_joke)
})

final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = final_chain.invoke({'topic': 'LangChain'})

print(result)

