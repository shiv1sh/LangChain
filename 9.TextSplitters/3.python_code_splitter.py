from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(chunk_size = 300, language = Language.PYTHON,chunk_overlap = 0)
text = """text = 
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a# filepath: /Users/shivanshchandravanshi/Learnings/GenAI/LangChain/LangChain/9.TextSplitters/3.python_code_splitter.py
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(chunk_size=300, language=Language.PYTHON, chunk_overlap=0)
"""

result = splitter.split_text(text)

print(result[0])