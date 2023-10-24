# Bring in deps
import os 
from bot import q_a

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# App framework
st.title('GPT App')
prompt = st.text_input('Ask any question about mental health here:') 

# Show stuff to the screen if there's a prompt
if prompt: 
    response = q_a(prompt)
    st.write(response) 
