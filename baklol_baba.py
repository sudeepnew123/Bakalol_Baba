from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
import random
import os

# Funny replies
baklol_lines = [
    "Beta, zindagi ek golgappa hai... kabhi teekha, kabhi meetha!",
    "Jo soya, woh roya... aur jo padha, woh bhi roya.",
    "Pyaar nahi, data pack chahiye zindagi me!",
    "Tension lene ka nahi... dene ka zamana hai!",
    "Jab tak hai Jio, tab tak hai hope!",
    "Jo log khud ki DP pe like karte hain, unse bach ke rehna.",
    "Aalsi log kal kare so aaj, aur aaj kare so kabhi nahi!",
    "Tumhara future bright hai... bas light chalu rehni chahiye!",
    "Zindagi me agar kuch banna hai... to 'baklol' banna!",
    "Bina padhe exam me pass hona... ek adhyatmik karishma hai.",
    "Chai garam ho ya tumhara gussa... dono se door hi acha hai!",
    "Mummy ka ‘5 minute me aaya’ = Akhand Brahm Vākya!"
]

gyan_lines = [
    "Zindagi ka asli maza to offline hone me hai.",
    "Jo chala gaya uske liye data kharch mat kar.",
    "Jab tak broken charger chal raha hai, tab tak hope hai.",
    "Dil nahi dard hota hai jab net slow hota hai.",
    "Safalta ek process hai... jisme failure update milte rehte hain.",
    "Jab tak tera crush online hai, tab tak hope bhi online hai.",
    "Paise se khushi nahi aati... par pizza zarur aata hai.",
    "Jo log 'seen' karke reply nahi karte... unka WiFi kabhi na chale!",
    "Agar zindagi me kuch nahi ho raha... to status update kar 'Feeling Spiritual'.",
    "Jo gyaan teri mummy tere sath roz share karti hai... woh Harvard me bhi nahi milega!"
]

sad_lines = [
    "Usne 'seen' kiya, par 'feel' nahi kiya...",
    "Dard dil me hai, par smile DP pe hai.",
    "Main 'last seen' tha uski life ka...",
    "Woh chala gaya... par WhatsApp ka status kabhi nahi badla.",
    "Dil mein thoda sa pain, aur phone mein thoda sa lag...",
    "Jab bhi uska naam aata hai, WhatsApp crash ho jata hai.",
    "Kuch rishte kabhi nahi bante... jaise slow internet.",
    "Kyunki aaj bhi uska status 'offline' hai, aur main 'online'.",
    "Woh chala gaya, par uska emoji ab bhi mere heart mein hai.",
    "Dil ke kone mein ek file hai, jisme 'broken' likha hai.",
    "Tere bina zindagi jaise WiFi bina internet.",
    "Dosti mein bhi dard hai, jaise broken earphones mein sound!"
]

breakup_lines = [
    "Breakup hua? Mubarak ho, ab free data bachega!",
    "Woh gayi... par password mat chhod dena.",
    "Rishte toot gaye, par memes ab bhi strong hai.",
]

# Command-based mentions
async def cmd_baklol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mention the user in the response
    if update.message.from_user.username:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"@{update.message.from_user.username} {random.choice(baklol_lines)}", 
            parse_mode="Markdown"
        )

async def cmd_gyan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mention the user in the response
    if update.message.from_user.username:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"@{update.message.from_user.username} Baklol Baba bolte hain:\n{random.choice(gyan_lines)}", 
            parse_mode="Markdown"
        )

async def cmd_sad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mention the user in the response
    if update.message.from_user.username:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"@{update.message.from_user.username} {random.choice(sad_lines)}", 
            parse_mode="Markdown"
        )

async def cmd_breakup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mention the user in the response
    if update.message.from_user.username:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"@{update.message.from_user.username} {random.choice(breakup_lines)}", 
            parse_mode="Markdown"
        )

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("baklol", cmd_baklol))
    app.add_handler(CommandHandler("gyan", cmd_gyan))
    app.add_handler(CommandHandler("sad", cmd_sad))
    app.add_handler(CommandHandler("breakup", cmd_breakup))

    print("Baklol Baba is live!")
    app.run_polling()

if __name__ == "__main__":
    main()
