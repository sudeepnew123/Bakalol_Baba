from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
import random, os

# Funny Lines
baklol_lines = [
    "Beta, zindagi ek golgappa hai... kabhi teekha, kabhi meetha!",
    "Jo padha, woh bhi roya!",
    "Jo log DP pe like karte hain... woh khatarnaak hote hain!",
    "Tumhara future bright hai... bas charger sahi ho!"
]

gyan_lines = [
    "Zindagi ka asli maza to offline hone me hai.",
    "Jo gaya uske liye data mat barbaad kar.",
    "Mummy ka gyaan = Harvard + Oxford",
]

sad_lines = [
    "Usne seen kiya, par feel nahi kiya...",
    "Main uski life ka 'last seen' tha.",
]

breakup_lines = [
    "Breakup hua? Mubarak ho, ab tum data bachaoge!",
    "Woh gayi... par password mat bhoolna.",
]

# Utils
def mention_name(user):
    return f"@{user.username}" if user.username else user.first_name

# Command Handlers
async def cmd_baklol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{mention_name(user)} {random.choice(baklol_lines)}")

async def cmd_gyan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{mention_name(user)} Baklol Baba bolte hain:\n{random.choice(gyan_lines)}")

async def cmd_sad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{mention_name(user)} {random.choice(sad_lines)}")

async def cmd_breakup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{mention_name(user)} {random.choice(breakup_lines)}")

# Mention or Reply Handler
async def mention_or_reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg.reply_to_message and msg.reply_to_message.from_user.id == context.bot.id:
        await msg.reply_text(f"{mention_name(msg.from_user)} {random.choice(baklol_lines)}")
    elif msg.entities:
        for entity in msg.entities:
            if entity.type == "mention" and context.bot.username.lower() in msg.text.lower():
                await msg.reply_text(f"{mention_name(msg.from_user)} {random.choice(baklol_lines)}")
                break

# Main
def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("baklol", cmd_baklol))
    app.add_handler(CommandHandler("gyan", cmd_gyan))
    app.add_handler(CommandHandler("sad", cmd_sad))
    app.add_handler(CommandHandler("breakup", cmd_breakup))

    # Mentions / Replies
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), mention_or_reply_handler))

    print("Baklol Baba is Live!")
    app.run_polling()

if __name__ == "__main__":
    main()
