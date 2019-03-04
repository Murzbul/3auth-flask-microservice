from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

config_db = {
    'driver': 'mysql',
    'user': 'auth',
    'password': 'auth',
    'host': 'auth_mysql',
    'port': 3306,
    'db': 'auth'
}

string_config_db = f'{config_db["driver"]}://{config_db["user"]}:{config_db["password"]}@{config_db["host"]}:{config_db["port"]}/{config_db["db"]}'
