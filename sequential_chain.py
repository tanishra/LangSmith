from CustomLLM import EuriChatModel
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

os.environ['LANGCHAIN_PROJECT'] = 'Sequential LLM APP'

EURI_API = os.getenv("EURI_API_KEY")

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = EuriChatModel(api_key=EURI_API)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

config = {
    'run_name' : 'sequential_chain',
    'tags' : ['llm_app','report generation','summarization'],
    'metadata' : {'model' : 'gpt-4.1-mini', 'model_temp' : 0.7, 'parser' : 'stroutputparser'}
}

result = chain.invoke({'topic': 'Unemployment in India'},config=config)

print(result)
