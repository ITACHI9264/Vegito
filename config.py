import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("unknown", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("6429312094:AAEOqUf63TKhlhbQXMK351aMeT7T0Th58Ck", default=None)
BOT_TOKEN2 = getenv("6418979594:AAE5jqgnZ4_XidMhSKZBobZmX22Unrn-fHY", default=None)
BOT_TOKEN3 = getenv("6820222596:AAEzXKW93B_UYdio4laAOfl2SjrDUiaenLs", default=None)
BOT_TOKEN4 = getenv("6386904092:AAGPROf9z9c1ZFVpIhXbDbPbihuPdps-jDA", default=None)
BOT_TOKEN5 = getenv("6762819248:AAGUnTCCqNnLr56qlXSwPEe6lRZP4k1GH6w", default=None)
BOT_TOKEN6 = getenv("6862422347:AAFuy5IOE2NngPZgDUDXzUsDNGm4olRl2ZA", default=None)
BOT_TOKEN7 = getenv("6627376941:AAGkrA3XRNFFwaDWX0xByMmLOQ-FstoJvR4", default=None)
BOT_TOKEN8 = getenv("6874339587:AAFdFuPUh_fiG9cIyiQnWccOMliCXGRUljA", default=None)
BOT_TOKEN9 = getenv("6629817418:AAFzwbRlov-iVBkGJW0j16hUVY1Fv-Ro774", default=None)
BOT_TOKEN10 = getenv("6795494957:AAHAyw0uQupVfSWXLMikCfCWXMUzgCQhsRo", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5867944994").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5867944994"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
