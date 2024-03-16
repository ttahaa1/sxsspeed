from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/95bc0cd9d859ddc13d28a.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/95bc0cd9d859ddc13d28a.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TT_11_TY")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TT_11_TY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6739845954").split()))


FAILED = "https://pin.it/4vxGamd0A"
