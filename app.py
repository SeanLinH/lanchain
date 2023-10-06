import os 
from langchain.llms import OpenAI
import streamlit as st
# from langchain.llms.utils. import PyPDFLoader



os.environ['OPENAI_API_KEY'] = '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'
llm = OpenAI(temperature=0.9)
prompt = st.text_input('蘆竹二廠GPT')


if prompt:
    response = llm(prompt)
    st.write(response)



