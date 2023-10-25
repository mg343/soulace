# Bring in deps
import os 
from apiKey_noPush import apikey

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConversationChain
import streamlit as st
from langchain.chains.conversation.memory import ConversationKGMemory

os.environ['OPENAI_API_KEY'] = apikey



#model overview
llm = OpenAI(model_name='text-davinci-003', 
             temperature=0, 
             max_tokens = 256)

template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. You will only use information contained in the "Relevant Information" section and will not hallucinate.

Relevant Information:

{history}

Human: {input}
Assistant:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

chatgpt_chain = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=prompt,
    memory=ConversationKGMemory(llm=llm),
)



# App framework
st.title('GPT App')



#message structure
if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about mental health!"}
    ]

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatgpt_chain.predict(input=prompt)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message) # Add response to message history
