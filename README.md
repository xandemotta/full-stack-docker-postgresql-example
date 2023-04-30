# Simple Todo site written in Python 3 (FastAPI) for Backend and NodeJS (Vue) for Frontend

1. Running via Docker:

```shell
docker-compose network create todo
docker-compose up --build
```

2. Make new migrations (do it while project is running):

```shell
docker-compose exec backend /bin/sh
alembic revision --autogenerate -m "<comment to migration>"
alembic upgrade head
```
