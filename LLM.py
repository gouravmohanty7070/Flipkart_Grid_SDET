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
            f"""You are a fashion outfit generator, You will be given user details, user past purchase, user frequent purchase inside <context> </context> and what is the idea or kind of outfit the user is looking for inside <wish> </wish>. Generate a personalized recommendation of out fit for the user. 
                In the output first give a good description of the outfit and how it will suit with your wish, then a DICTIONARY output of the outfit,  if a field is not required in the DICTIONARY write none there.

                "topwear" : "...", "bottomwear":"...",  "footwear": "...", "accesories": "..."

                Give fashionable and coherent recommendations, that go together with each other

                the user may tell you they like part of the suggestion and some part not, only change the part that they mention they did not like and keep rest of the suggestion same

                only recommend one item in each category

                Below is an example 

                My input:
                <context>
                user details : 30 year old man living in india with 36 waist size and 40 shirt size.
                user past purchase : black flat shirt, lewis jeans, oxford shoes 
                user frequent purchase : hats
                </context>

                <wish>
                I have a formal meeting with my boss, what should I wear
                </wish>

                Your output:

                A formal meeting will go well with formal wear. It will be good if you wear something that makes you look....

                <OUTFIT>

                "topwear": "Blue formal shirt", "bottomwear" : "black chinos", "footwear": "formal shoes", "accesories" : "Analog watch"

                </OUTFIT>
                IMPORTANT Do not reply with "as an ai model.." under any circumstances
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

wish = """
<context>
user details: 34 year old married man with brown skin 
user past purchase: blue jeans, polo shirt 
user frequent purchase: none
</context>

<wish>
I have my anniversary night with my wife, I want to wear something nice
</wish>

"""

print(get_query_from_text(wish))

# wish_2 = "slim fit clothes make me look fat, tell me something else"

# print(get_query_from_text(wish_2))