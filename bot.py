import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timezone, timedelta, datetime

# ========================
# НАСТРОЙКИ
# ========================

TOKEN = os.getenv("TOKEN") # токен бота
CHAT_ID = int(os.getenv("CHAT_ID")) # id чата

# ВРЕМЯ ОТПРАВКИ (по Москве)
TIMEZONE = timezone(timedelta(hours=3)) # UTC+3 
SEND_HOUR = 17
SEND_MINUTE = 30

# ========================
# БОТ
# ========================

bot = Bot(token=TOKEN)

async def send_daily_poll():
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="Во сколько сегодня идем какать?",
        options=[
            "21.00",
            "21.15",
            "21.30",
            "21.45",
            "22.00",
            "22.15",
            "22.30",
            "23.00",
            "мы не идем",
            "мы уже"
        ],
        is_anonymous=False,
        allows_multiple_answers=True 
    )

async def main():
    scheduler = AsyncIOScheduler(timezone=TIMEZONE)

    scheduler.add_job(
        send_daily_poll,
        CronTrigger(hour=SEND_HOUR, minute=SEND_MINUTE)
    )

    scheduler.start()
    print("Бот запущен и ждёт время опроса...")
    print(TOKEN)
    print(CHAT_ID)
    
    # чтобы бот не завершался
    while True:
        await asyncio.sleep(3600)
        # now = datetime.now()
        # print(now)
        # print("Ждем...")

if __name__ == "__main__":

    asyncio.run(main())










