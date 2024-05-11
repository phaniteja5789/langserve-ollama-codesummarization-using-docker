This repository details out the code summarization using the Langchain framework with LangServe, Ollama and docker.

The sourcecode.py is the entry point for the application.

This project is developed in 2 phases

phase-1

	
	The prompt has been developed using PromptTemplate
	
	And using the PromptTemplate and the LLM a langchain Chain is created. And the chain will be invoked whenever the endpoint will be hit since its been integrated with LangServe
	
	The Langserve internally uses the FastAPI uvicorn server and it will be running in the port 8080 of the Local host.
	
	A Dockerfile is created in order to build a image, which uses the uvicorn server in order to run an API in the port 8080.
	
	
	After completion of Phase-1, the image the build.
	
phase-2

	
	The DockerCompose.yaml is created, in this compose file, there are 2 images are used.
	
	1st Image
		
		In this Image, the Ollama image will be pulled from the repository and it will be running in the port 11434
		
		The model that I am using is llama3 and it will be saved in the /root/.ollama
		
	2nd Image
	
		In this Image, the Langserve endpoint will be running which uses the Langchain Chain in order to generate the summary for the method and the result will be shown in the output of the LangServe Playground
		

The final output is shown as below

		