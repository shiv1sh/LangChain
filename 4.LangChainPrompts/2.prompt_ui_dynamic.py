from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st
load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

st.header('Research Tool')

paper_input = st.selectbox('Select a paper', ['Attention is all you need', 'BERT: Pre-training of Deep Bidirectional Transformers (2018)', 'NeRF: Neural Radiance Fields (2020)'])

style_input = st.selectbox('Select a style', ['Summary', 'Key Points', 'Strengths and Weaknesses'])

length_input = st.selectbox('Select a length', ['Short', 'Medium', 'Long'])


template = PromptTemplate(
    template=""""
You are a research assistant.

Paper: {paper_input}

Provide a {style_input} of this paper.
Response length: {length_input}.

Make the explanation clear and easy to understand.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button('Submit'):
    result = model.invoke(prompt)
    st.write(result.content)
