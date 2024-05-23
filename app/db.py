from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(getenv("DATABASE_URI", "mongodb://localhost:27017/"))
database = client.testdb
