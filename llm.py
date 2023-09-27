#pip install langchain huggingface_hub google-generativeai

import os
# from langchain.llms import HuggingFaceHub
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
#
# template = """What is the opposite of the following word?
#
# {user_input}
#
# Answer: The opposite is: """
#
# prompt = PromptTemplate(template=template, input_variables=["user_input"])
#
# llm_chain = LLMChain(prompt=prompt,
#                      llm=HuggingFaceHub(repo_id="google/flan-t5-large",
#                                         model_kwargs={"temperature":0,
#                                                       "max_length":64}))
#
#
# def run_llm(user_input):
#     llm_answer = llm_chain.run(user_input=user_input)
#     return llm_answer
#
# answer = run_llm("happy")
# print(answer)



### --------------------- google ----------------------- ###
import google.generativeai as palm
key = os.getenv('google_key')

palm.configure(api_key=key)

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]

for m in models:
    print(f"Model Name: {m.name}")

model = models[0].name

prompt = """What is the opposite of the following word? Answer with only the opposite word.

fire

Answer: The opposite is: """

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.2,
    max_output_tokens=64,
)

def run_llm():
    result = completion.result
    return result
