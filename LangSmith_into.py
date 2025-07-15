from langsmith import LangSmith, LLM

# Initialize LangSmith with your API key
langsmith = LangSmith(api_key="your API key")

# Define your LLM (ChatGPT)
llm = LLM("gpt-4", api_key="open ai api_key")

# Track interactions with LangSmith
response = langsmith.track(llm, "Your prompt here")

# Output the response
print(response)
