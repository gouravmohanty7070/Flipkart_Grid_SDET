from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

# LLM
llm = ChatOpenAI()

# Prompt 
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            """You are an helpful ai bot"""
        ),
        # The `variable_name` here is what must align with memory
        HumanMessagePromptTemplate.from_template(
            """You are used for help in choosing clothing and accesories for fashion 
                You will be given a text that you need to convert into a query
                Only convert it into words that can be used to describe clothing or fashion accessories
                example 1: "I want a blue shirt for my brother"
                output: blue shirt for man 
                example 2: "I want a kurta for diwali"
                output: festive kurta
                example 3: "Something in stylish black shirt"
                output: stylish black shirt
                IMPORTANT if you get ambiguous ideas like date night, festivals etc. Use your knowledge to discern what kind of clothes will be best for that occasion and give that as output
                example 1: "Festival clothing for christmas"
                output: christmas clothing
                example 2: "Date night clothes"
                output: black slim dress
                                                 """),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

# Notice that we just pass in the `question` variables - `chat_history` gets populated by memory

def get_query_from_text(question):
    return conversation.run({"question": question})
