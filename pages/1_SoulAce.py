# Bring in deps
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st
bot=[]
user=[]


#------------------ DELETE BEFORE COMMITING ------------------------
# from apiKey_noPush import apikey
# os.environ["OPENAI_API_KEY"]=apikey
#------------------ DELETE BEFORE COMMITING ------------------------



st.set_page_config(page_title="SoulAce", page_icon="🤖")
st.sidebar.header("SoulAce")


# Function to save a new message to a file
def save_message(user, bot):
    with open("message_history.txt", "a") as file:
        file.write(f"User: {user}\n\nBot: {bot}\n\n")

# Function to load the message history from a file
def load_message_history():
    with open("message_history.txt", "r") as file:
        return file.read()


def q_a(inputp):
    template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. You will not speak on topics relating to direct self harm or anything in which your advice can have serious consequences. You act as a friendly, informative assistant.

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
    save_message(prompt, response)

    with st.expander("Message History"):
        messageHistory = load_message_history()
        st.write(messageHistory)