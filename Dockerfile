FROM python:3.7-slim-buster

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "run.py", "--bind", "0.0.0.0", "--port", "8085"]
