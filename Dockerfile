FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install Flask

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]
