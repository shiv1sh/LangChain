from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size = 10, chunk_overlap = 0, separators = ['\n\n', '\n', ' ', ''])

text = 'This is a sample text to demonstrate the recursive character text splitter.'

result = splitter.split_text(text)
print(len(result))
print(result)