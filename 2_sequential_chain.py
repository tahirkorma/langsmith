from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGCHAIN_PROJECT'] = 'Sequential LLM App'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", temperature= 0.7)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

config = {
    'run_name': 'sequential chain',
    'tags': ['sequential llm', 'report generation', 'google gemini'],
    'metadata': {'model': 'gemnini 2.0 flash', 'model_temp': 0.7, 'parser': 'stroutputparser'}
}


result = chain.invoke({'topic': 'rise of mughals'}, config=config)

print(result)
