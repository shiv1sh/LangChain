from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
load_dotenv()

class Review(TypedDict):
    summary : str
    sentiment : Annotated[str, 'Describe the sentiment of the review as positive, negative or neutral']

    # we can add the description of the keys in the dictionary using Annotated, 
    # this will help us to understand the purpose of each key and also it will help us to generate better output from the model
    pros : Annotated[Optional[str], 'List the pros of the movie, if any']
    cons : Annotated[Optional[str], 'List the cons of the movie, if any']

model = ChatOpenAI(model = 'gpt-4')

structured_output_model = model.with_structured_output(Review)

result = structured_output_model.invoke("What do you think about the movie 'Inception'?")

print(result)