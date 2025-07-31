import os

from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

DATABASE_NANE = 'BookShop'
BOOK_COLLECTION = 'books'

API_KEY = 'jhjkfdhgjfdhjk63565655'
