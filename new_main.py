# Bring in deps
import os
from apiKey_noPush import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConversationChain  
from langchain.chains.conversation.memory import ConversationKGMemory

os.environ['OPENAI_API_KEY'] = apikey

# Model 
llm = OpenAI(model_name='text-davinci-003', temperature=0, max_tokens=256)

# Prompt 
template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. You will only use information contained in the "Relevant Information" section and will not hallucinate. Relevant Information: {history} Human: {input} Assistant:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Chain
chatgpt_chain = ConversationChain(
    llm=llm, 
    prompt=prompt,
    memory=ConversationKGMemory(llm=llm)  
)

# App
st.title('Mental Health Chat')

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, I'm here to chat about mental health."}]

user_input = st.text_input("You: ")

if user_input:

  st.session_state.messages.append({"role": "user", "content": user_input})
  with st.spinner("Thinking..."):
    response = chatgpt_chain.predict(st.session_state.messages)

  st.session_state.messages.append({"role": "assistant", "content": response})

  for msg in st.session_state.messages: 
    st.write(msg["content"], msg["role"])