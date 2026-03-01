from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate summary of the following {text}',
    input_variables = ['text']
)
prompt2 = PromptTemplate(
    template = 'Generate 5 questions based on the following {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Combine the {notes} and the {questions} to generate a comprehensive report',
    input_variables = ['notes', 'questions']
)

model = ChatOpenAI(model = 'gpt-4.1-nano')

output_parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model | output_parser,
    'questions' : prompt2 | model | output_parser
})

# print(notes)

merge_chain = prompt3 | model | output_parser

chain = parallel_chain | merge_chain

result = chain.invoke({'text': '''Shivansh sir, yeh raha 100 words on LangChain

LangChain is an open-source framework designed to build applications powered by large language models (LLMs). It helps developers connect LLMs with external data sources, APIs, and tools to create intelligent workflows. LangChain supports chains, agents, memory, and retrieval mechanisms like RAG (Retrieval-Augmented Generation). Developers can structure prompts, manage conversation history, and integrate vector databases for semantic search. It works with models from OpenAI and others. LangChain is widely used for chatbots, document Q&A systems, automation tools, and agentic AI applications. It simplifies orchestration, making LLM-based applications more modular, scalable, and production-ready.'''})

print(result)


chain.get_graph().print_ascii()  # Visualize the chain graph

# print(result)