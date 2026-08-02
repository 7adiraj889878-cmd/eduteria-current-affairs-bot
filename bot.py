import os
import asyncio

asyncio.set_event_loop(asyncio.new_event_loop())

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Welcome to EDUTERIA Current Affairs Bot!")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
