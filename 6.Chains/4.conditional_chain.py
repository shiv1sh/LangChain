from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from dotenv import load_dotenv

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class FeedBack(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='The sentiment of the text')


parser1 = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object = FeedBack)

prompt1 = PromptTemplate(
    template = 'Classify the text as either "positive" or "negative" \n {text} \n {format_instructions}',
    input_variables = ['text'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template = 'Generate appropriate response based on the positive feedback \n {feedback}',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Generate appropriate response based on the negative feedback \n {feedback}',
    input_variables = ['feedback']
)

model = ChatOpenAI(model = 'gpt-4.1-nano')

# this chain can provide the output other than 'positive' or 'negative' as well, which is not what we want. So we will use the parser2 to ensure that the output is either 'positive' or 'negative'
# chain = prompt1 | model | parser1

classifier_chain = prompt1 | model | parser2
positive_chain = prompt2 | model | parser1
negative_chain = prompt3 | model | parser1

result = classifier_chain.invoke({'text' : 'I Love using LangChian'}).sentiment  # Output: 'positive'

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_chain),
    (lambda x: x.sentiment == 'negative', negative_chain),
    RunnableLambda(lambda x: 'Invalid feedback')
)
# result = chain.invoke('I love using LangChain!')  # Output: 'positive'

chain = classifier_chain | branch_chain

print(chain.invoke({'text' : 'This is a terrible experience'}))

chain.get_graph().print_ascii()
