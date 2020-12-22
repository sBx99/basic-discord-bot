# handles all environment variables
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

def discord_credentials():
    DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
    DISCORD_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    DISCORD_PUBLIC_KEY = os.getenv('PUBLIC_KEY')
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

    return DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, DISCORD_PUBLIC_KEY, DISCORD_TOKEN

def imgur_credentials():
    IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
    IMGUR_CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')

    return IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

def reddit_credentials():
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
    return REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT