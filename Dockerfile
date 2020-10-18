FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /

ENV DATABASE_URL=postgres://lain@localhost:5432/users 
#add your own postgres url

COPY ./app /app 