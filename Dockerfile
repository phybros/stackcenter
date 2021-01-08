FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ADD backend/requirements.txt /app
RUN pip3 install -r requirements.txt

ADD backend /app
ADD frontend/dist /app/static

ADD https://github.com/docker/compose/releases/download/1.27.4/docker-compose-Linux-x86_64 /app

EXPOSE 5000
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
