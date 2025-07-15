from langchain_openai import OpenAI
import os



# Option 2: Directly pass the API key as a named parameter
llm = OpenAI(temperature=0.9, openai_api_key="openai_api_key")

response = llm("Tell me a joke.")
print(response)
