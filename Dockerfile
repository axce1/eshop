FROM python:3.6-alpine

RUN apk update
RUN apk add build-base
RUN apk add jpeg-dev
RUN apk add zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib


ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN ["chmod", "+x", "/code/start-dev.sh"]
RUN ["/code/start-dev.sh"]
