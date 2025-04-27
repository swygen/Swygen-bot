from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaAnimation
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7870153726:AAHNAJWQpMhk2UXe1iXwWBiNC59ojAMnbO8'  # BotFather থেকে পাওয়া টোকেন বসাও

# ভাষা সেটাপ
USER_LANGUAGE = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    USER_LANGUAGE[user_id] = 'en'  # Default language English

    # Lottie Animation (GIF version, কারণ টেলিগ্রাম সরাসরি Lottie JSON সাপোর্ট করে না)
    animation_url = "https://lottie.host/bf854b13-2663-4694-b082-9df976286f02/qxAoPgiNsp.lottie"

    await context.bot.send_animation(chat_id=update.effective_chat.id, animation=animation_url)

    welcome_text = "👋🏻 **Welcome to Developer Help Bot!**\n\nPlease select your language:"
    keyboard = [
        [InlineKeyboardButton("🇧🇩 বাংলা", callback_data='set_lang_bn')],
        [InlineKeyboardButton("🇬🇧 English", callback_data='set_lang_en')],
    ]
    await update.message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def language_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'set_lang_bn':
        USER_LANGUAGE[user_id] = 'bn'
    else:
        USER_LANGUAGE[user_id] = 'en'

    await send_main_menu(update, context)

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    lang = USER_LANGUAGE.get(user_id, 'en')

    text_en = "🏡 **Main Menu**\n\nChoose what you want to explore:"
    text_bn = "🏡 **প্রধান মেনু**\n\nআপনি কী জানতে চান?"

    keyboard = [
        [InlineKeyboardButton("👤 About Me", callback_data='about')],
        [InlineKeyboardButton("🛠️ Skills", callback_data='skills')],
        [InlineKeyboardButton("🌐 Website", callback_data='website')],
        [InlineKeyboardButton("📞 Contact", callback_data='contact')],
        [InlineKeyboardButton("👨‍💻 Developer", callback_data='developer')],
        [InlineKeyboardButton("📜 Privacy Policy", callback_data='privacy')],
        [InlineKeyboardButton("🗂️ Projects", callback_data='projects')],
    ]

    text = text_en if lang == 'en' else text_bn
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    lang = USER_LANGUAGE.get(user_id, 'en')

    await query.answer()

    back_button = [InlineKeyboardButton("🔙 Back", callback_data='back_to_menu')]

    if query.data == 'about':
        if lang == 'en':
            text = "👤 **About Me**\n\nHi, I'm Ayman Hasan Shaan, passionate about Web Development and Automation."
        else:
            text = "👤 **আমার সম্পর্কে**\n\nআমি আয়মান হাসান শান, ওয়েব ডেভেলপমেন্ট এবং অটোমেশন নিয়ে কাজ করি।"

    elif query.data == 'skills':
        if lang == 'en':
            text = "🛠️ **Skills**\n\n- Python\n- HTML, CSS, JS\n- Telegram Bots\n- Automation Scripts"
        else:
            text = "🛠️ **স্কিলস**\n\n- পাইথন\n- এইচটিএমএল, সিএসএস, জাভাস্ক্রিপ্ট\n- টেলিগ্রাম বটস\n- অটোমেশন স্ক্রিপ্টস"

    elif query.data == 'website':
        text = "🌐 Visit my website: [Click Here](https://swygen.netlify.app/)"

    elif query.data == 'contact':
        if lang == 'en':
            text = "📞 **Contact Info**\n\n- Email: swygenofficial@gmail.com\n- Telegram: @Swygen_bd"
        else:
            text = "📞 **যোগাযোগের তথ্য**\n\n- ইমেইল: swygenofficial@gmail.com\n- টেলিগ্রাম: @Swygen_bd"

    elif query.data == 'privacy':
        text = "📜 [Read our Privacy Policy](https://swygen.netlify.app/police)"

    elif query.data == 'developer':
        text = "👨‍💻 **Developer**\n\nBot developed by Swygen Official."

    elif query.data == 'projects':
        if lang == 'en':
            text = "🗂️ **My Projects**\n\n- Project 1\n- Project 2\n- Project 3"
        else:
            text = "🗂️ **আমার প্রজেক্টসমূহ**\n\n- প্রজেক্ট ১\n- প্রজেক্ট ২\n- প্রজেক্ট ৩"

    elif query.data == 'back_to_menu':
        await send_main_menu(update, context)
        return

    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([back_button]), parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to restart the bot.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CallbackQueryHandler(language_selected, pattern='^set_lang_'))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()
