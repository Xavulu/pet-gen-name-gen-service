FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /

COPY ./app /app 