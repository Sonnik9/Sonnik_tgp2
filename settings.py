import os
from dotenv import load_dotenv

# sudo apt install ffmpeg

load_dotenv()

class Settings:
    API_TOKEN = os.getenv("API_TOKEN", "")
    API_KEY_CHAT_GPT = os.getenv("API_KEY_CHAT_GPT", "")
    URL_CHAT_GPT = os.getenv("URL_CHAT_GPT", "")

settings = Settings()

# import os

# class Settings:
#     API_TOKEN = os.environ.get("API_TOKEN")
#     API_KEY_CHAT_GPT = os.environ.get("API_KEY_CHAT_GPT")
#     # URL_CHAT_GPT = os.getenv("URL_CHAT_GPT", "")

# settings = Settings()


