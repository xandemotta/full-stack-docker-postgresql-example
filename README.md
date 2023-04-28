# Simple Todo site written in Python 3 (FastAPI) for Backend and NodeJS (Vue) for Frontend

Running:
1. Rename `.env.simple` to `.env` and setting it
2. Install dependencies use:

```shell
pip install -U pipenv
pipenv install
```

3. Running:

```shell
docker-compose up --build
```

4. Make new migrations (do it while project is running):

```shell
docker-compose exec web /bin/sh
alembic revision --autogenerate -m "<comment to migration>"
alembic upgrade head
```
