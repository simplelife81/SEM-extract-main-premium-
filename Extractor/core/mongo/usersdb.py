from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

mongo = AsyncIOMotorClient(MONGO_URL)

db = mongo["sem_extract"]
users_col = db["users"]


async def get_users():
    users = []
    async for u in users_col.find():
        users.append(u["user"])
    return users


async def get_user(user):
    return await users_col.find_one({"user": user})


async def add_user(user):
    if not await get_user(user):
        await users_col.insert_one({"user": user})


async def del_user(user):
    await users_col.delete_one({"user": user})
