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
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()

print(data)

try:
    products = data["info"]["products"]

    for product in products:

        name = product.get("goods_name", "No Name")
        price = product.get("salePrice", {}).get("amount", "N/A")

        image = product.get("goods_img")

        caption = f"""
🛍 {name}

💰 Price: ₹{price}

#shein #deal
"""

        bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=image,
            caption=caption
        )

except Exception as e:
    print(e)
