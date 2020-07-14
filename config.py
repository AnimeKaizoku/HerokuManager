import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","awoo")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","uguu")
    AUTHORIZED_USERS = [792109647,353689802,660565862]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","weeaboo")
