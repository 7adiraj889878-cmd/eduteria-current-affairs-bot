import os
import asyncio

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Welcome to EDUTERIA Current Affairs Bot!")

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
