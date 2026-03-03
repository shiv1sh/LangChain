from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url = 'https://quotes.toscrape.com/'
loader = WebBaseLoader(url)

docs = loader.load()

model = ChatOpenAI(model = 'gpt-4.1-nano')
prompt = PromptTemplate(
    template = 'Answer the following question \n {question} from the given text \n {text}',
    input_variables = ['question', 'text']
)
output_parser = StrOutputParser()
chain = prompt | model | output_parser

result = chain.invoke({
    'question': 'what is provided in the text',
    'text' : docs[0].page_content
})
print(result)
