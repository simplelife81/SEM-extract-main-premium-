from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

mongo = AsyncIOMotorClient(MONGO_URL)

db = mongo["sem_extract"]
premium_col = db["premium"]


async def add_premium(user_id, expire_date):
    await premium_col.update_one(
        {"_id": user_id},
        {"$set": {"expire_date": expire_date}},
        upsert=True
    )


async def remove_premium(user_id):
    await premium_col.delete_one({"_id": user_id})


async def check_premium(user_id):
    return await premium_col.find_one({"_id": user_id})


async def premium_users():
    users = []
    async for data in premium_col.find():
        users.append(data["_id"])
    return users
