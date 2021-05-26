import os

class Config:

    env = os.environ

    DEBUG = True

    MYSQL_USER = env.get("MYSQL_USER", "")
    MYSQL_PORT = int(env.get("MYSQL_PORT", 0))
    MYSQL_DB = env.get("MYSQL_DB", "")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD", "")
    MYSQL_HOST = env.get("MYSQL_HOST", "")

    MYSQL_CURSORCLASS=env.get("MYSQL_CURSORCLASS", "DictCursor")
