# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/test_for_cellosign
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
# copy project
COPY . /usr/src/test_for_cellosign

# run entrypoint.sh
ENTRYPOINT ["/usr/src/test_for_cellosign/entry.sh"]
