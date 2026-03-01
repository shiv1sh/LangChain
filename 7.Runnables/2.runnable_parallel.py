from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv 
load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a post for LinkedIn on the topic \n {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a post for Tweeter on the topic \n {topic}',
    input_variables = ['topic']
)

output_parser = StrOutputParser()

model = ChatOpenAI(model = 'gpt-4.1-nano')

parallel_chain = RunnableParallel({
    'linkedIn_post': RunnableSequence(prompt1, model, output_parser),
    'twitter_post': RunnableSequence(prompt2, model, output_parser)
})

result = parallel_chain.invoke({'topic' : 'AI'})

print(result['linkedIn_post'])
print(result['twitter_post'])