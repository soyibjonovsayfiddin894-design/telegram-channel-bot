from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8145646747:AAHEWPad_dj_9vn2xgAHLwz4RW-_0ratEys"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\n"
        "Men kanalingizdagi postlarning oxiriga "
        "@kanal_nomi ko‘rinishida havola qo‘shaman.\n\n"
        "Talablar:\n"
        "1) Kanal public bo‘lishi\n"
        "2) Bot admin bo‘lishi (Edit messages)\n"
        "3) Yangi post tashlanishi\n\n"
        "Tamom."
    )


async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if post is None:
        return

    chat = post.chat
    username = chat.username

    # Kanal public bo‘lmasa chiqamiz
    if not username:
        return

    link_text = f"\n\n@{username}"

    # 📝 Matnli post
    if post.text:
        if link_text not in post.text:
            await post.edit_text(post.text + link_text)

    # 📸 Rasm + caption
    elif post.photo:
        caption = post.caption or ""
        if link_text not in caption:
            await post.edit_caption(caption + link_text)

    # 🎥 Video + caption
    elif post.video:
        caption = post.caption or ""
        if link_text not in caption:
            await post.edit_caption(caption + link_text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))

    print("BOT ISHGA TUSHDI")
    app.run_polling()


if __name__ == "__main__":
    main()