# Bring in deps
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page
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
st.title('SoulAce: Mental Health Assistant')

with st.expander("SoulAce Usage Instructions", expanded=True):
    st.write("\n\n**SoulAce is programmed as a 'single session' chatbot, to ensure user security and reduce environmental impact.**\nAs a 'single session' bot, **SoulAce does not preserve memory between responses.**\nTo allow SoulAce to respond as best as possible, **please explain your question as in-depth as possible.**\nIf outputted information is crucial to the question, such as in the case of expanding on a concept, **it is advised to prompt SoulAce with a summarized version of the response in question, along with your specific question,** assuming the summary is within the text limit.")
    st.write("\n\nFree instance of the SoulAce mental-health resource. Responses are not a replacement for the expertise of mental health professionals.")
    st.write("\n\nUsers are responsible for their interactions with Soulace and their mental health decisions. We are not liable for the consequences of these decisions.")
    if st.button("View SoulAce Usage Guidelines"):
        switch_page("Guidelines")

prompt = st.text_input('Ask SoulAce a question about mental health here:', max_chars=256) 

# Show stuff to the screen if there's a prompt
if prompt:
    response = q_a(prompt)
    st.write(response)
    if st.button("For more help from recognized organizations, visit the Resources page by clicking here."):
        switch_page("Resources")
    with st.expander("To reduce economical and environmental impact, Users are recommended to limit usage of SoulAce.", expanded=False):
        st.write("""
SoulAce is powered by large servers, and **overusage of the resource can cause damage to the environment** around the server setup.""")
        st.write("""
**In accordance with our pro-environment policies, users are recommended to limit their usage of SoulAce.**""")
        st.write("""
As a free resource, there is **no actual boundary to how much SoulAce can be prompted.**""")
        st.write("""

However, **every run of SoulAce has both a financial, and environmental cost.** """)
        st.write("""

**Steps implemented at every step in the development process attempt to minimize this impact, but running any app, let alone providing users with speedy responses, requires heavy server load.**""")
        st.write("""

Therefore, **reducing the amount of prompts SoulAce handles is advised.**""")
else:
    if st.button("For more help from recognized organizations, visit the Resources page by clicking here."):
        switch_page("Resources")
    with st.expander("To reduce economical and environmental impact, Users are recommended to limit usage of SoulAce.", expanded=False):
        st.write("""
SoulAce is powered by large servers, and **overusage of the resource can cause damage to the environment** around the server setup.""")
        st.write("""
**In accordance with our pro-environment policies, users are recommended to limit their usage of SoulAce.**""")
        st.write("""
As a free resource, there is **no actual boundary to how much SoulAce can be prompted.**""")
        st.write("""

However, **every run of SoulAce has both a financial, and environmental cost.** """)
        st.write("""

**Steps implemented at every step in the development process attempt to minimize this impact, but running any app, let alone providing users with speedy responses, requires heavy server load.**""")
        st.write("""

Therefore, **reducing the amount of prompts SoulAce handles is advised.**""")
