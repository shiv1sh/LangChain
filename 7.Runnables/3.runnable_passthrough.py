from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a Joke on the topic \n {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'explain the joke \n {joke}',
    input_variables = ['joke']
)

output_parser = StrOutputParser()

model = ChatOpenAI(model = 'gpt-4.1-nano')

joke_generator_chain = RunnableSequence(prompt1, model, output_parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, output_parser)
})

final_chain = joke_generator_chain | parallel_chain

result = final_chain.invoke({'topic' : 'Langchain'})

print('Here is the joke:', result['joke'])
print('Explanation:', result['explanation'])
final_chain.get_graph().print_ascii()
