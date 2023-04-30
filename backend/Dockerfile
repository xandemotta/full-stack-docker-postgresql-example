FROM python:3.10

WORKDIR /code

RUN pip install -U pip

RUN pip install -U pipenv
COPY Pipfile* /code/
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src /code/
