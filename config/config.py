import os
from dotenv import load_dotenv

load_dotenv()


config = {
	"DB_DATABASE_NAME": os.getenv("DB_DATABASE_NAME"),
	"DB_USERNAME": os.getenv("DB_USERNAME"),
	"DB_PASSWORD": os.getenv("DB_PASSWORD"),
	"DB_PORT": int(os.getenv("DB_PORT")),
	"DB_HOST": os.getenv("DB_HOST"),
}