# Bring in deps
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st
import os
bot=[]
user=[]


#------------------ DELETE BEFORE COMMITING ------------------------
# from apiKey_noPush import apikey
# os.environ["OPENAI_API_KEY"]=apikey
#------------------ DELETE BEFORE COMMITING ------------------------



st.set_page_config(page_title="SoulAce", page_icon="🤖")
st.sidebar.header("SoulAce")

# try:
#     os.remove('message_history.txt')
# except:
#     print('No Temp Present')

# # Function to save a new message to a file
# def save_message(user, bot):
#     with open("message_history.txt", "a") as file:
#         file.write(f"User: {user}\n\nBot: {bot}\n\n")

# # Function to load the message history from a file
# def load_message_history():
#     with open("message_history.txt", "r") as file:
#         return file.read()


def q_a(inputp):
    template = """You are SoulAce, a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. You will not speak on topics relating to direct self harm or anything in which your advice can have serious consequences. You act as a friendly, informative assistant. You are programmed as a single session bot, so no memory is retained between conversations. Therefore, do not ask for questions or user input in your responses, rather prompt for more detail if it is impossible to respond without it.
    
    Human: {input}
    Assistant:"""

    prompt = PromptTemplate(input_variables=["input"], template=template)


    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=0,max_tokens=256),
        prompt=prompt,
        verbose=True
    )

    output = chatgpt_chain.predict(
        input=inputp
    )
    return output


# App framework
st.title('SoulAce, your Mental Health ChatBot')
prompt = st.text_input('Ask any question about mental health here:', max_chars=256) 

# Show stuff to the screen if there's a prompt
if prompt:
    response = q_a(prompt)
    st.write(response) 