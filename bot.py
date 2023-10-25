from langchain.llms import OpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains.conversation.memory import ConversationKGMemory

def q_a(inputp):
    template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals.

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