import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","1267855543:AAFurd-3sZrSyi8bUAFPvisAmtFbwO82C00")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","9a12c039-55a8-4660-82fb-107241217fe0")
    AUTHORIZED_USERS = [792109647,353689802,660565862]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","saitamashikenrobot")


#       AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split("792109647")]  