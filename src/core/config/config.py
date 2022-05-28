from envparse import env

env.read_envfile('.env')

POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_DATABASE = env.str('POSTGRES_DATABASE')

DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    database=POSTGRES_DATABASE
)
