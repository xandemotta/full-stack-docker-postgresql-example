# Simple Todo API powered by Python 3 and FastAPI

Rename `.env.simple` to `.env` and setting it

To install dependencies use:
```shell
pip install -U pipenv
pipenv install
```

Starting:
```shell
docker-compose up --build
```

To make new migrations (do it while project is running):
```shell
docker-compose exec web /bin/sh
alembic revision --autogenerate -m "<comment to migration>"
alembic upgrade head
```
