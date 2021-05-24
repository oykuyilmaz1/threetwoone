import os

class Config:

    env = os.environ

    DEBUG = True

    MYSQL_USER = env.get("MYSQL_USER", "root")
    MYSQL_PORT = int(env.get("MYSQL_PORT", 3306))
    MYSQL_DB = env.get("MYSQL_DB", "showsdb")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD", "Cmpe.321Demo")
    MYSQL_HOST = env.get("MYSQL_HOST", "127.0.0.1")

    MYSQL_CURSORCLASS=env.get("MYSQL_CURSORCLASS", "DictCursor")
