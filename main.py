import requests
from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID

bot = Bot(token=BOT_TOKEN)

url = "https://www.sheinindia.in/api/category/sverse-5939-37961"

params = {
    "currentPage": 1,
    "pageSize": 5,
    "format": "json"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.sheinindia.in/",
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

print("STATUS:", response.status_code)
print(response.text[:500])

try:
    data = response.json()

    print(data)

except Exception as e:
    print("JSON ERROR:", e)
