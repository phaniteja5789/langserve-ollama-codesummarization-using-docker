This repository details out the code summarization using the Langchain framework with LangServe, Ollama and docker.

The sourcecode.py is the entry point for the application.

This project is developed in 2 phases

phase-1

	
	The prompt has been developed using PromptTemplate
	
	And using the PromptTemplate and the LLM a langchain Chain is created. And the chain will be invoked whenever the endpoint will be hit since its been integrated with LangServe
	
	The Langserve internally uses the FastAPI uvicorn server and it will be running in the port 8080 of the Local host.
	
	A Dockerfile is created in order to build a image, which uses the uvicorn server in order to run an API in the port 8080.
	
	
	After completion of Phase-1, the image is built with the name langservecontainer.

 	Framework used in this Phase are langchain

  	Modules used in this Phase are 

   		langchain_community.llms.ollama import Ollama ==> in order to use Ollama where the llama3 model will be running in the local host at port 11434
     	        langserve import add_routes ==> used to run the Chain at the endpoint 8080.
       		langchain.prompts import PromptTemplate ==> used the PromptTemplate in order to create a Prompt that needs to be sent to the LLM.
	
phase-2

	
	The DockerCompose.yaml is created, in this compose file, there are 2 images are used.
	
	1st Image
		
		In this Image, the Ollama image will be pulled from the repository and it will be running in the port 11434
		
		The model that I am using is llama3 and it will be saved in the /root/.ollama
		
	2nd Image
	
		In this Image, the Langserve endpoint will be running which uses the Langchain Chain in order to generate the summary for the method and the result will be shown in the output of the LangServe Playground
		

The final output is shown as below
![LangServeUI](https://github.com/phaniteja5789/langserve-ollama-codesummarization-using-docker/assets/36558484/a41e74af-2836-4d60-be9e-9dd9e107ec97)

The prompt that is sent to the LLM(llama3) using Ollama in order to run the LLM locally is as below screenshot.
![InputPrompt](https://github.com/phaniteja5789/langserve-ollama-codesummarization-using-docker/assets/36558484/632c46b7-d8b6-4c19-aaf7-9c2fe473a0c5)



		
