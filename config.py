# ═══════════════════════════════════════════════════════════
#        😎  VISHAL MUSIC BOT  😎
#   GitHub : github.com/ItsMeVishal0/VishalMusic
#   Developer : @ItsMeVishalBots | Telegram
#   Module : Bot Configuration & Environment Variables
# ═══════════════════════════════════════════════════════════

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ─────────────────────────────────────────────────────────
API_ID = int(getenv("API_ID", 39636887))
API_HASH = getenv("API_HASH", "58d9e9789942f13dfeae5a58aadc967c")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 8922591120))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Devil_Shiva_op")
BOT_USERNAME = getenv("BOT_USERNAME", "RIdhii_Music_bot")
BOT_NAME = getenv("BOT_NAME", "≽ ^⎚  𝐑ɪᴅʜɪ ꭙ 𝐌𝐮𝐬𝐢𝐜  ⎚^ ≼")
ASSUSERNAME = getenv("ASSUSERNAME", "≽ ^⎚  𝐑ɪᴅʜɪ ꭙ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 ⎚^ ≼")

# ── Database & logging ────────────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1003967121724))

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "3221225472"))  # 3 GB
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "3221225472"))  # 3 GB
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL", "https://pastebin.com/RurxsvMF")
API_URL = getenv("API_URL")        # optional
API_KEY = getenv("API_KEY")        # optional 
DEEP_API = getenv("DEEP_API")      # optional

# ── Telegram Bot API (Local Server for colored buttons support) ───────────────
# If you run a local Telegram Bot API server, set this to its URL.
# Example: http://localhost:8081  or  http://127.0.0.1:8081
# Without this, button color (style) fields will be ignored by Telegram.
# Setup guide: https://github.com/tdlib/telegram-bot-api
LOCAL_BOT_API_URL = getenv("LOCAL_BOT_API_URL", "").rstrip("/")

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ItsMeVishal0/VishalMusic.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+SnUd5iJTEqY3YzUx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+zwBuaQ7xctFlYjVl")
# Link used by the /privacy command (set your own privacy-policy post/page)
PRIVACY_LINK = getenv("PRIVACY_LINK", SUPPORT_CHAT)

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ──────────────────────────────────────────────────────────
START_IMGS = [
    "https://files.catbox.moe/a6sz5r.jpg",
    "https://files.catbox.moe/53szdj.jpg",
    "https://files.catbox.moe/h9dan0.jpg",
    "https://files.catbox.moe/s8yhxr.jpg",
]
STICKERS = [
    "CAACAgUAAyEFAASQje-AAAI92mkOFHmOlyKv0vEpoJE6S7ZInIuPAALbFQACSZmpVI0wvAnbSnk9HgQ",
    "CAACAgQAAyEFAASQje-AAAI92GkOFFx4j5i7GwlGsRbvXBaZbgquAAIoFQACir5JU9xIMA-J9yY7HgQ",
    "CAACAgQAAyEFAASQje-AAAI91mkOFEeMiZrau4LoUgHQAuhfVUNoAAJbHQACmKWIUVKzS9qKs-juHgQ",
    "CAACAgUAAyEFAASQje-AAAI91GkOFDevrsTZ_JzDdyHdsu2VhsvHAAJ2EwAC_xfYVo5iQw7a3JPfHgQ",
    "CAACAgUAAyEFAASQje-AAAI90mkOFCn95GwjE62nWBG2o9H-FK15AAJgFQACJ_uwVMGj96qQgd3hHgQ",
    "CAACAgQAAyEFAASQje-AAAI90GkOFCDWtQkvBiumJxSoedz0NqvLAAIzFAAC9ED4UX1Ta6URzlyIHgQ",
]
HELP_IMG_URL = "https://files.catbox.moe/a6sz5r.jpg"
PING_VID_URL = "https://files.catbox.moe/qibmue.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/h9dan0.jpg"
STATS_VID_URL = "https://files.catbox.moe/a6sz5r.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/s8yhxr.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/a6sz5r.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/h9dan0.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/a6sz5r.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/a6sz5r.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Search Messages (Single Line) ───── #
# {0} = user mention/name
AYU = [
    
    "𝐅ɪɴᴅɪɴɢ 𝐘ᴏᴜʀ 𝐒ᴏɴɢ ꨄ︎ {0} ",
    "𝐒ᴇᴀʀᴄʜɪɴɢ 𝐁ᴇ𝐬ᴛ 𝐓ʀᴀᴄᴋ ♡ {0} ",
    "𝐋ᴏᴀᴅɪɴɢ 𝐌ᴜ𝐬ɪᴄ ✦ {0} ",
    "𝐘ᴏᴜʀ 𝐕ɪʙᴇ 𝐈𝐬 𝐂ᴏᴍɪɴɢ ꨄ︎ {0} ",
    "𝐏ʟᴀʏɪɴɢ 𝐒ᴏᴏɴ 𝐁ᴀʙʏ ♡ {0} ",
    "𝐆ᴇᴛᴛɪɴɢ 𝐑ᴇᴀᴅʏ 𝐅ᴏʀ 𝐘ᴏᴜ ✦ {0} ",
    "𝐇ᴏʟᴅ 𝐎ɴ 𝐁ᴀʙᴇ ꨄ︎ {0} ",
    "𝐌ᴜ𝐬ɪᴄ 𝐋ᴏᴀᴅɪɴɢ 𝐅ᴏʀ ♡ {0} ",
    "𝐀ʟᴍᴏ𝐬ᴛ 𝐑ᴇᴀᴅʏ 𝐉ᴀᴀɴ ꨄ︎ {0} ",
    "𝐏ʀᴇᴘᴀʀɪɴɢ 𝐘ᴏᴜʀ 𝐓ʀᴀᴄᴋ ✦ {0} ",
    
]

AYUV = [
    "💌✨ ʜᴇʏ {0} 💞🌸\n\n🎶 ɪ'ᴍ {1} 💖 ʏᴏᴜʀ ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴜꜱɪᴄ ʙᴏᴛ 🎧🔥\n\n┣━━━━━━━━━━━━━━━⧫\n┃ 🌟 ꜱᴛʀᴇᴀᴍ ᴍᴜꜱɪᴄ ɪɴ ᴠᴄ\n┃ 🎵 ʏᴏᴜᴛᴜʙᴇ • ꜱᴘᴏᴛɪꜰʏ • ᴊɪᴏꜱᴀᴀᴠɴ\n┃ ⚡ ꜰᴀꜱᴛ & ꜱᴍᴏᴏᴛʜ ᴘʟᴀʏʙᴀᴄᴋ\n┃ 💫 24x7 ᴍᴜꜱɪᴄ ᴠɪʙᴇꜱ\n┗━━━━━━━━━━━━━━━⧫\n\n💖 ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ & ꜱᴛᴀʀᴛ ᴛʜᴇ ᴘᴀʀᴛʏ 🎉",

    "🌹✨ ᴡᴇʟᴄᴏᴍᴇ {0} 💕\n\n🎧 {1} ɪꜱ ʜᴇʀᴇ ᴛᴏ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴠᴄ ᴀᴡᴇꜱᴏᴍᴇ 💫🔥\n\n┣━━━━━━━━━━━━━━━⧫\n┃ 🎶 ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴍᴜꜱɪᴄ\n┃ 🚀 ꜰᴀꜱᴛ ꜱᴛʀᴇᴀᴍɪɴɢ\n┃ 💞 ᴍᴜʟᴛɪ-ᴘʟᴀᴛꜰᴏʀᴍ ꜱᴜᴘᴘᴏʀᴛ\n┃ 🌸 ꜱᴍᴀʀᴛ & ᴇᴀꜱʏ ᴄᴏᴍᴍᴀɴᴅꜱ\n┗━━━━━━━━━━━━━━━⧫\n\n✨ ᴛʏᴘᴇ /play ᴀɴᴅ ᴇɴᴊᴏʏ ɴᴏɴ-ꜱᴛᴏᴘ ᴍᴜꜱɪᴄ 🎵🦋"
]

# ── Runtime structures ──────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ──────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    COOKIE_URL = None

# Only allow these cookie link formats
if COOKIE_URL and not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")
    
    
print("""
╔════════════════════════════════════╗
║🎵   𝐑ɪᴅʜɪ ꭙ 𝐌𝐮𝐬𝐢𝐜  
╚════════════════════════════════════╝
""")

# ═══════════════════════════════════════════════════════════
#        😎  VISHAL MUSIC BOT  😎
#   github.com/ItsMeVishal0/VishalMusic
# ═══════════════════════════════════════════════════════════
