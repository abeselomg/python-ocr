FROM python:3.9.2-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
# RUN pip install -r requirements.txt


RUN pip install Flask
RUN pip install easyocr
RUN pip install opencv-python-headless


# copy project
COPY . /usr/src/app/