# Don't Edit

import os
from dotenv import load_dotenv

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "21159773"))
API_HASH = os.environ.get("API_HASH", "49ae08543a07335e195756eba2f56e11")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7068360749:AAGtY1VHoI4MxtWLt1OA0fqfjWsMu70ah8M")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("7303665128")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://aaroha:aaroha@cluster0.jxsimkw.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "7303665128")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(7303665128)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002231063697")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "updates_chnle") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
