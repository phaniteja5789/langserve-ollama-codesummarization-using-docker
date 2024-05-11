from langchain_community.llms.ollama import Ollama
from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import PromptTemplate
import uvicorn

app = FastAPI(
    title="Get Summary for the given method",
    version="1.0",
    description="A simple api which gives the summary for the given method",
)

llm = Ollama(model='llama3', temperature=0.1)

prompt = PromptTemplate(
        template='''
        Generate the summary for the method that is passed as an argument in a string format which should only describe the core logic of the method
        and shouldn't worry about the input arguments or the return type or the method name or any example for the below method and it needs
        to return only the summary of the core logic not like "The summary of the method" like that:
        \n\n {method}''',
        
        input_variables=["method"]
    )


add_routes(
    app,
    prompt | llm,
    path="/summary",
)


#if __name__ == "__main__":
 #   uvicorn.run(app, host="localhost", port=8080)