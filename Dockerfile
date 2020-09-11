FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /

COPY * /app/static/corpi_json 


RUN pip install -r /requirements.txt

COPY ./app /app 