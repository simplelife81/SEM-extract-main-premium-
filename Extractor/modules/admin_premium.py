
from pyrogram import Client, filters
from datetime import datetime, timedelta
from Extractor.core.mongo.plans_db import add_premium, remove_premium
from config import OWNER_ID

@Client.on_message(filters.command("addpremium") & filters.user(OWNER_ID))
async def add_premium_cmd(client, message):
    try:
        user_id = int(message.command[1])
        days = int(message.command[2])
        expire_date = datetime.utcnow() + timedelta(days=days)
        await add_premium(user_id, expire_date)
        await message.reply(f"✅ Premium added for {days} days")
    except:
        await message.reply("Usage: /addpremium user_id days")

@Client.on_message(filters.command("removepremium") & filters.user(OWNER_ID))
async def remove_premium_cmd(client, message):
    try:
        user_id = int(message.command[1])
        await remove_premium(user_id)
        await message.reply("❌ Premium removed")
    except:
        await message.reply("Usage: /removepremium user_id")
