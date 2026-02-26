
import asyncio
from datetime import datetime
from Extractor.core.mongo.plans_db import premium_col

async def expiry_checker(bot):
    while True:
        now = datetime.utcnow()
        async for user in premium_col.find():
            expire = user.get("expire_date")
            if expire and expire < now:
                await premium_col.delete_one({"_id": user["_id"]})
        await asyncio.sleep(300)  # check every 5 minutes
