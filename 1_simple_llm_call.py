from dotenv import load_dotenv
from CustomLLM import EuriChatModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

EURI_API = os.getenv("EURI_API_KEY")

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = EuriChatModel(api_key=EURI_API)
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the recipe of pasta"})
print(result)
