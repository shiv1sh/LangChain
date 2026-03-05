from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

chunker = SemanticChunker(OpenAIEmbeddings(), breakpoint_threshold_type='standard_deviation', breakpoint_threshold_amount = 1)
text = """
Artificial Intelligence is transforming the way humans interact with machines. 
Modern AI systems use large datasets and neural networks to learn patterns and 
make predictions. Companies around the world are investing heavily in AI research 
to automate tasks, improve decision making, and build intelligent assistants.

Space exploration has always fascinated humans. Scientists send satellites and 
spacecraft to study distant planets, stars, and galaxies. Missions to Mars and 
the Moon aim to understand the origins of our solar system and explore the 
possibility of human settlements beyond Earth.

Health and fitness play a crucial role in maintaining a balanced life. 
Regular exercise improves cardiovascular health, strengthens muscles, and 
reduces stress levels. Eating nutritious food and getting proper sleep are 
equally important for overall well-being.

Cricket is one of the most popular sports in many countries. The game is played 
between two teams of eleven players and involves batting, bowling, and fielding. 
Major tournaments like the World Cup bring millions of fans together to celebrate 
the sport and support their favorite teams.
"""
docs = chunker.create_documents([text])
print(len(docs))
print(docs)
