FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requierments.txt /code/
RUN pip install -r requierments.txt
COPY . /code/
