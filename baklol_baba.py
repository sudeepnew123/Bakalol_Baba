from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
import random, os

# Funny Lines
breakup_lines = [
    "Breakup hua? Mubarak ho, ab tum data bachaoge!",
    "Woh gayi... par password mat bhoolna.",
    "Rishte toot gaye, par memes ab bhi strong hai.",
    "Ab tumhara status ‘Single & Lagging’ hai.",
    "Breakup se zyada battery low hone ka dard hota hai.",
    "Woh tere life se gayi... tera Netflix bhi le gayi.",
    "Ex ko ‘Goodbye’ kehna asaan hota hai... jab tak uska naam recharge offer me na aaye.",
    "Usne tera dil toda... tu login kar 'Recovery Mode' me.",
    "Woh chali gayi... Tune password change nahi kiya?",
    "Dard ka password ‘Ex@2023’ hai!",
    "Jab tak memory card me uski photo hai... tu free nahi hai!",
    "Woh aakhri seen bhi delete nahi hota...",
    "Breakup hua? Achha hai, tumhare memes me jaan aa gayi.",
    "Woh ab bhi meri gallery me baithi hai.",
    "Tere jaise ex ke liye to auto-reply ‘bye’ hona chahiye!",
    "Tera pyaar bhi uss internet jaisa tha... slow aur kabhi kabhi.",
    "Uske baad tu toh Airtel user ban gaya... no connection!",
    "Tera breakup hua ya phone ka reset?",
    "Woh chali gayi, tune kya kiya? Screenshot delete!",
    "Rishte khatam, login bhi logout.",
    "Breakup ke baad toh pizza bhi emotional lagta hai.",
    "Tere ex ka ‘last seen’ ab bhi tera heartbreak karta hai.",
    "Usne kaha block kar diya... par tu ab bhi status check karta hai.",
    "Breakup ke baad dard ka level: DND mode!",
    "Usne ‘It’s not you, it’s me’ bola... aur chalti bani!",
    "Tu ab bhi uske liye active hai... jaise unused app.",
    "Tera love story us recycle bin me pada hai.",
    "Woh relationship ek monthly pack tha... khatam ho gaya!",
    "Breakup ke baad banda khud ka motivational speaker ban jaata hai.",
    "Woh chali gayi... data bach gaya, par dil nahi!"
    "Beta, zindagi ek golgappa hai... kabhi teekha, kabhi meetha!",
    "Jo padha, woh bhi roya!",
    "Jo log DP pe like karte hain... woh khatarnaak hote hain!",
    "Tension lene ka nahi... dene ka zamana hai!",
    "Baklol Baba bolte hain — mere owner Sudeep se poochh lo!",
    "Mujhe sab aata hai... par Sudeep better batayega!",
    "Tumhara future bright hai... agar Sudeep approve kare toh!",
    "Zindagi me kuch bhi impossible nahi... agar Sudeep haan kar de!",
    "Aaj ka gyaan? Pehle Sudeep se poochh lo!",
    "Main kuch bhi bol sakta hoon... par Sudeep hi final hai!",
    "Jab tak Sudeep ne like nahi kiya... tab tak kuch viral nahi hota!",
    "Main sirf baklol hoon... Sudeep toh ultimate guru hai!",
    "Sawal mushkil hai? Sudeep se poochh lo!",
    "Ye mat mujhse puchho... mere owner Sudeep se poochh lo!",
    "Tere jaise baklol ke liye sirf Sudeep ka ashirvaad kaafi hai!",
    "Main toh chill hoon... Sudeep hi mastermind hai!"
]

gyan_lines = [
    "Zindagi offline ho toh hi asli sukoon hai.",
    "Jo chala gaya uske liye MB mat barbaad kar.",
    "Jab tak broken charger chal raha hai, tab tak hope hai.",
    "Dil nahi, dard hota hai jab net slow hota hai.",
    "Safalta ek process hai... jisme failure update milte rehte hain.",
    "Jo log 'seen' karke reply nahi karte... unka WiFi kabhi na chale!",
    "Paise se khushi nahi aati... par pizza zarur aata hai.",
    "Kabhi kabhi bas phone ko mute karna hi mental peace hota hai.",
    "Aaj ka gyaan — Sudeep se pucho, Baklol Baba ab busy hai!",
    "Sudeep se gyaan lo... main toh sirf comedy karta hoon!",
    "Jo waqt pe online ho jaye... wohi asli dost hai!",
    "Zindagi ek meme hai... serious log usse samajh nahi paate.",
    "Sudeep ne kaha hai — bina chai ke gyaan mat do!",
    "Choti choti baaton ka screenshot mat lo... zindagi zoom hoti hai!",
    "Jab tak mobile silent hai, tab tak dosti safe hai!",
    "Baklol Baba bolte hain — gyaan kam, chill zyada karo!",
    "Tension lene se better hai... Sudeep se suggestion le lo!",
    "Zindagi hard hai... par Sudeep ke memes harder!",
    "Agar kuch samajh na aaye, toh Baklol Baba nahi... Sudeep best guide hai!",
    "Pyaar fail ho sakta hai, par Sudeep ka logic nahi!",
    "Jab tak Sudeep reply kare, tab tak WhatsApp pe bhajan suno.",
    "Kabhi kabhi life ka best lesson ek failed screenshot hota hai.",
    "Sudeep ne bola — jo gaya uska data bhi delete kar do!",
    "Chinta chhodo... Sudeep sab set karega!",
    "Baklol Baba bas bolta hai, par Sudeep sach dikhata hai!",
    "Aaj ka mantra: Sudeep + Chai = Peace!",
    "Sudeep se dosti ho jaaye, toh sad status bhi funny lagta hai.",
    "Gyaan sabke paas hota hai... par Sudeep ke paas logic bhi hai!",
    "Baklol Baba bolte hain — seekhne ka mood ho toh Sudeep se seekho!",
    "Zindagi ke har sawaal ka ek hi answer — Sudeep se poochh lo!"
]

sad_lines = [
    "Usne seen kiya, par feel nahi kiya...",
    "Main uski life ka 'last seen' tha.",
    "Dil mein dard hai, par DP pe smile hai.",
    "Woh online hai, par mere liye nahi...",
    "Mera toh ek hi sapna tha... uska 'Hi' aana.",
    "Woh chala gaya... aur mera ringtone bhi uda le gaya.",
    "Aaj bhi uske messages delete nahi kiye...",
    "Tere bina zindagi... WiFi bina net jaisi hai.",
    "Tumhare bina sab kuch hai, par kuch bhi nahi!",
    "Jab tu gaya... battery bhi fast khatam hone lagi.",
    "Woh status badalti rahi... main emotions.",
    "Rishte wahi ache hote hain... jo screenshots me rehte hain.",
    "Main toh uska backup ban gaya, jab main primary tha...",
    "Har sad song me tera chehra dikhai deta hai.",
    "Mera toh DP bhi sirf tere liye tha...",
    "Tu chali gayi... par login details le gayi!",
    "Yaad uski aati hai... jab phone silent hota hai.",
    "Uski ek 'Hi' bhi recharge jaisi thi...",
    "Tera last message ab bhi pinned hai.",
    "Woh achanak se online aa jaaye... bas isi umeed pe zinda hoon.",
    "Dil toh bacha hai... par tera password bhi usme save hai.",
    "Woh har baar 'Typing…' dikhata tha... kabhi send nahi karta.",
    "Uska last seen meri neend chura leta hai.",
    "Tu vo memory hai... jo delete se pehle confirm maangta hai.",
    "Meri feelings us SIM jaisi ho gayi hai... jo ab band hai.",
    "Ab toh ringtone bhi uski hansi sun ke ro padti hai.",
    "Tere bina lagta hai Google Maps bhi rasta bhool gaya.",
    "Har baar hope karta hoon... tu ek baar 'seen' kar le.",
    "Main emoji bhejta tha, woh 'hmm' karta tha.",
    "Sad hoon, lekin meme to daily daal raha hoon..."
]

breakup_lines = [
    "Breakup hua? Mubarak ho, ab tum data bachaoge!",
    "Woh gayi... par password mat bhoolna.",
    "Rishte toot gaye, par memes ab bhi strong hai.",
    "Ab tumhara status ‘Single & Lagging’ hai.",
    "Breakup se zyada battery low hone ka dard hota hai.",
    "Woh tere life se gayi... tera Netflix bhi le gayi.",
    "Ex ko ‘Goodbye’ kehna asaan hota hai... jab tak uska naam recharge offer me na aaye.",
    "Usne tera dil toda... tu login kar 'Recovery Mode' me.",
    "Woh chali gayi... Tune password change nahi kiya?",
    "Dard ka password ‘Ex@2023’ hai!",
    "Jab tak memory card me uski photo hai... tu free nahi hai!",
    "Woh aakhri seen bhi delete nahi hota...",
    "Breakup hua? Achha hai, tumhare memes me jaan aa gayi.",
    "Woh ab bhi meri gallery me baithi hai.",
    "Tere jaise ex ke liye to auto-reply ‘bye’ hona chahiye!",
    "Tera pyaar bhi uss internet jaisa tha... slow aur kabhi kabhi.",
    "Uske baad tu toh Airtel user ban gaya... no connection!",
    "Tera breakup hua ya phone ka reset?",
    "Woh chali gayi, tune kya kiya? Screenshot delete!",
    "Rishte khatam, login bhi logout.",
    "Breakup ke baad toh pizza bhi emotional lagta hai.",
    "Tere ex ka ‘last seen’ ab bhi tera heartbreak karta hai.",
    "Usne kaha block kar diya... par tu ab bhi status check karta hai.",
    "Breakup ke baad dard ka level: DND mode!",
    "Usne ‘It’s not you, it’s me’ bola... aur chalti bani!",
    "Tu ab bhi uske liye active hai... jaise unused app.",
    "Tera love story us recycle bin me pada hai.",
    "Woh relationship ek monthly pack tha... khatam ho gaya!",
    "Breakup ke baad banda khud ka motivational speaker ban jaata hai.",
    "Woh chali gayi... data bach gaya, par dil nahi!"
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
