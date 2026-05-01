import asyncio
import schedule
import time
from datetime import date
from telegram import Bot
import pytz

TOKEN = "8365149140:AAFDPgSxy3eCAVY_69WTvX8sQeftY_DbhWo"
CHAT_ID = -5091244581
CONCERT_DATE = date(2026, 5, 29)
EVENT_NAME = "концерта Канье Уэста"

async def send_countdown():
    bot = Bot(token=TOKEN)
    today = date.today()
    days_left = (CONCERT_DATE - today).days

    if days_left > 0:
        message = f"🎤 До {EVENT_NAME} осталось {days_left} дней!"
    elif days_left == 0:
        message = f"🔥 Сегодня {EVENT_NAME}! Наслаждайся!"
    else:
        message = f"✅ Концерт уже прошёл {abs(days_left)} дней назад."

    await bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Отправлено: {message}")

def job():
    asyncio.run(send_countdown())

# Ташкент = UTC+5
# 10:00 утра по Ташкенту = 05:00 UTC
# 22:00 вечера по Ташкенту = 17:00 UTC
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("17:00").do(job)

print("Бот запущен! Отправка в 10:00 и 22:00 по Ташкенту")
job()

while True:
    schedule.run_pending()
    time.sleep(30)
