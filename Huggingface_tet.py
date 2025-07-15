from transformers import pipeline
from langchain.llms import HuggingFace

# Initialize the Hugging Face pipeline for text generation
hf_pipeline = pipeline("text-generation", model="gpt2")

# Define a wrapper class to use with LangChain
class HuggingFaceLLM(HuggingFace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pipeline = hf_pipeline

    def __call__(self, prompt, **kwargs):
        response = self.pipeline(prompt, **kwargs)
        return response[0]['generated_text']

# Create an instance of your LLM
api_key ="your api_key"
llm = HuggingFaceLLM(api_key)

# Generate a response
response = llm("Tell me a joke.")
print(response)



