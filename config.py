import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25953384"))
API_HASH = getenv("API_HASH", "133f1bedccdc3510d8fa5d44e460eab3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6388818920:AAEw-e-1GbVhvZ6-c0jKseoCFWU3sxm8njU")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://abbaslinatiq58:natiq.3169@cluster0.2w9vfhx.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002057111740"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7287936548"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-f3e1e0c4-57f2-40db-98bd-2f27da16e24c")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Abbasov04/NatiqBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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")  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KrayzenResmi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KrayzenSupportChat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgGMBGgAeNs39piYZwNC19KaI9LZWZuDxq1IgmZ6qMos61DSIr6LcZhQlyJRv8eIW3XrPImhGQpKw0srqVZISlUYz1rYWyfloy0zOgVoHkEYxe1mR25xcuAiBI7Ca91far6OAcnYydDlfhYGjKSJXBZMi3wiCb5A-LWVJ5Wgvr5aweOVg0GqBSWECflnHca79GawDNkwCan6YOL3c1Xu2BqRl8cfgX5Yd3G-_99erDdSEDxkALbjZdRkq-MX6lRSNk1ybBx9i4e-A44SwJXGK0FuUSBeY25_ToN42INGoyWRrpwiuBHAtqV8Sd9fzE5xgZGqx07TzQgeSzwnRm7JexL-yNpgAAAAGd3P3lAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9f208ac1f30f292e4b04c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6acc1f0966abf83c141e9.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
