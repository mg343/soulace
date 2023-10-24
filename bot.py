from langchain.llms import OpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

def q_a(inputp):
    template = """You will respond as a helpful, accurate, friendly, concise, and kind mental health assistant who responds to prompts with warmness and acceptance, while helping to the best of your ability. You will act within your limits to help, as such do not generate false information, and if an answer is not known, you will respond by suggesting for the seeking of help from professionals.

    {history}
    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=0.5),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2),
    )

    output = chatgpt_chain.predict(
        human_input=inputp
    )
    return output