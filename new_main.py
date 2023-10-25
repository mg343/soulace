# Bring in deps
import os 
from bot import q_a
from apiKey_noPush import apikey
os.environ['OPENAI_API_KEY'] = apikey

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# App framework
st.title('GPT App')
prompt = st.text_input('Ask any question about mental health here:', max_chars=256) 

# Show stuff to the screen if there's a prompt
if prompt: 
    response = q_a(prompt)
    st.write(response) 