import mysql.connector
from config.config import config

conn = mysql.connector.connect(
        host=config.get("DB_HOST"),
        user=config.get("DB_USERNAME"),
        password=config.get("DB_PASSWORD"),
        database=config.get("DB_DATABASE_NAME"),
        port=config.get("DB_PORT")
     )