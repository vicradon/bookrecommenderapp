FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

RUN apt-get update && apt-get install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD service nginx start && python app.py