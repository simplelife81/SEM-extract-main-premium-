import os

# Telegram Config
API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Helpto_allbot")

# Channels (NO SPACE before -100)
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003700223671"))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003700223671"))
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003700223671"))

# MongoDB (READY TO USE)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://semuser:sempass123@cluster0.mongodb.net/sem_extract?retryWrites=true&w=majority"
)

# Other optional configs
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))
