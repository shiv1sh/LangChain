# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='HuggingFaceH4/zephyr-7b-beta',
#     task = 'text-generation',
#     provider="hf-inference" 
# )
# model = ChatHuggingFace(llm = llm)

# result = model.invoke('what is the capital of delhi')

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text2text-generation",
    provider="hf-inference"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of delhi")
print(result)