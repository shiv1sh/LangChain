from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


st.header('Enter the Prompt')
user_input = st.text_input('Enter you prompt here')
model = OpenAI(model = 'gpt-4')
if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)