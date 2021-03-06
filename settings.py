import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_CONNECT_URL = 'mongodb+srv://{}:{}@cluster0.vwwky.mongodb.net/{}?retryWrites=true&w=majority'.format(
    MONGO_DB_USERNAME,
    MONGO_DB_PASSWORD,
    MONGO_DB_NAME,
)
