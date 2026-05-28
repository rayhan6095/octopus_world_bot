import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

def scan_url(url):
    bad = ["login", "otp", "password", "bank", "verify"]
    score = sum(2 for b in bad if b in url.lower())

    if score >= 4:
        return "🔴 DANGEROUS"
    elif score >= 2:
        return "🟠 SUSPICIOUS"
    return "🟢 SAFE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 SOC Security Bot Online\n\n"
        "/scan <url>"
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = " ".join(context.args)

    if not url:
        await update.message.reply_text("⚠️ Give a URL")
        return

    result = scan_url(url)

    await update.message.reply_text(
        f"🌐 Scan Result:\n{result}"
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))

print("🤖 BOT RUNNING...")
app.run_polling()
