from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 9143931))
API_HASH = getenv("API_HASH", "5dcaf3b395762de3172651527214da4d")
BOT_TOKEN = getenv("BOT_TOKEN", "6054586380:AAGh0oYvdxUU1cI13JHcj_UG4RIZq4AOJZs")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
