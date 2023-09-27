#pip install langchain huggingface_hub

import os

from langchain import PromptTemplate, HuggingFaceHub, LLMChain
key = os.getenv('HUGGINGFACEHUB_API_TOKEN')

template = """What is the opposite of the following word?

{user_input}

Answer: The opposite is: """

prompt = PromptTemplate(template=template, input_variables=["user_input"])

llm_chain = LLMChain(prompt=prompt,
                     llm=HuggingFaceHub(repo_id="google/flan-t5-large",
                                        model_kwargs={"temperature":0,
                                                      "max_length":64}))

def run_llm(user_input):
    llm_answer = llm_chain.run(user_input=user_input)
    return llm_answer
