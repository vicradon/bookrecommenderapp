FROM python:3.9-slim AS flask-build

WORKDIR /app

COPY requirements.txt .

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt

COPY . /app/

RUN apt-get update && apt-get install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

STOPSIGNAL SIGINT

CMD service nginx start && python app.py
