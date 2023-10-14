FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /app1

ADD . /app1

COPY ./requirements.txt /app1/requirements.txt

RUN pip install -r requirements.txt

COPY . /app1
