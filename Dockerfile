FROM python:3.9-slim

WORKDIR /app

COPY requirements.text .
RUN pip install -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED 1
EXPOSE 5000

STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["app.py"]
