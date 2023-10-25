from langchain.llms import OpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains.conversation.memory import ConversationKGMemory

def q_a(inputp):
    template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals.

    {history}
    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


    chatgpt_chain = LLMChain(
        llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0,max_tokens=256),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2),
    )

    output = chatgpt_chain.predict(
        human_input=inputp
    )
    return output



def init_model():

    llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0,max_tokens=256),

    template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals. You will only use information contained in the "Relevant Information" section and will not hallucinate.

    Relevant Information:

    {history}

    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


    chatgpt_chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=ConversationKGMemory(llm=llm),
    )

    output = chatgpt_chain.predict(
        human_input=inputp
    )
    return output