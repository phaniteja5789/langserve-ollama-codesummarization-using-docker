FROM python:latest

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn","app.sourcecode:app","--host","0.0.0.0","--port","5050"]