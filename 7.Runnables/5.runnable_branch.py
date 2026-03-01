from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Genetrate a report on this topic \n {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a summary of this report \n {report}',
    input_variables = ['report']
)

output_parser = StrOutputParser()

model = ChatOpenAI(model = 'gpt-4.1-nano')

report_generation_chain = RunnableSequence(prompt1, model, output_parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())> 300, RunnableSequence(prompt2, model, output_parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generation_chain, branch_chain)

result = final_chain.invoke({'topic' : 'LangChain'})

print(result)