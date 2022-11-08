# syntax=docker/dockerfile:1

FROM python:3.11.0-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY playground playground

EXPOSE 8000

CMD [ "uvicorn", "playground.app:app", "--host", "0.0.0.0", "--port", "8000" ]
