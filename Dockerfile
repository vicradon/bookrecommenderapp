FROM python:3.9-slim AS flask-build

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

STOPSIGNAL SIGINT

###########################

FROM nginx AS runner

RUN apt-get update && apt-get install -y python3 python3-pip

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=flask-build /app /app

WORKDIR /app

EXPOSE 80

ENV PYTHONUNBUFFERED 1

CMD ["sh", "-c", "ls -la"]
# CMD ["sh", "-c", "nginx && python3 app.py"]