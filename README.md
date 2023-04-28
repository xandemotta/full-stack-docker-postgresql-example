# Simple Todo API powered by Python 3 and FastAPI

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
