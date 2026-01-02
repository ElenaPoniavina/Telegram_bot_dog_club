import os
import asyncio
import time
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timezone, timedelta

# ========================
# НАСТРОЙКИ
# ========================

TOKEN = os.getenv("TOKEN") # токен бота
CHAT_ID = int(os.getenv("CHAT_ID")) # id чата

# ВРЕМЯ ОТПРАВКИ (по Москве)
TIMEZONE = timezone(timedelta(hours=5)) # UTC+3
SEND_HOUR = 23
SEND_MINUTE = 45

# ========================
# БОТ
# ========================

bot = Bot(token=TOKEN)

def main():
    print("Бот запущен и ждёт время опроса...")
    print(TOKEN)
    print(CHAT_ID)

    bot.send_poll(
        chat_id=CHAT_ID,
        question="Во сколько сегодня идем какать?",
        options=[
            "20.30",
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
        is_anonymous=False
    )

    time.sleep(300)
    
if __name__ == "__main__":

    main()











