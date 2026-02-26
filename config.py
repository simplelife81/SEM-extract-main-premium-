import os

# Telegram Config
API_ID = int(os.environ.get("API_ID", "32546882"))
API_HASH = os.environ.get("API_HASH", "81254ed5acbeb5839a3493a995994864")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8507577912:AAE8HDhJSlaumOr4ftPF6oWuaEV7D2q-OHI")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Semextract_bot")

# Channels (NO SPACE before -100)
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003700223671"))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003700223671"))
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003700223671"))

# MongoDB (READY TO USE)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://semuser:sempass123@cluster0.mongodb.net/sem_extract?retryWrites=true&w=majority&appName=Cluster0"
)

# Other optional configs
OWNER_ID = int(os.environ.get("OWNER_ID", "1806771298"))
