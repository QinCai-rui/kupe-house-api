FROM python:3.14.0a6-slim-bookworm

WORKDIR /app

RUN pip install flask flask-cors flask_limiter requests

COPY app/ ./

CMD ["python", "run.py"]
