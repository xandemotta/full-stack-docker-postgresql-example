FROM python:3.9

WORKDIR /code

COPY Pipfile* /code/
RUN pip install -U pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src /code/
