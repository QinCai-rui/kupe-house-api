FROM python:3.14.0a6-slim-bookworm

WORKDIR /app

RUN pip install flask flask-cors

COPY app/ ./

CMD ["python", "run.py"]
