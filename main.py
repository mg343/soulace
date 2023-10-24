# Bring in deps
import os 
from bot import q_a
from apikey import apikey

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('GPT App')
prompt = st.text_input('Ask any question about mental health here:') 

# Prompt templates
# title_template = PromptTemplate(
#     input_variables = ['topic'], 
#     template='You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. Prompt: {topic}'
# )


# # Llms
# llm = OpenAI(temperature=0.9) 
# title_chain = LLMChain(llm=llm, prompt=title_template)

# Show stuff to the screen if there's a prompt
if prompt: 
    response = q_a(prompt)
    st.write(response) 
