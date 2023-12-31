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
#     llm_answer = llm_chain.run(user_input)
#     return llm_answer



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


player_word = None
npc_word = None


def run_llm(player_word, npc_word):
    prompt = f"""Two words are going to fight. Which of the following words wins?
    
    {player_word} VS {npc_word}
    
    Answer: The word that would win is: """

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=32,
    )

    result = completion.result
    return result
