from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇬🇧 English", callback_data='lang_en'),
         InlineKeyboardButton("🇧🇩 বাংলা", callback_data='lang_bn')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(
        photo="https://i.postimg.cc/7PQgNm10/20250427-172406.jpg",  # তোমার Banner ছবি
        caption="✨ **Welcome to Developer SwygeN Bot!**\n\nSelect your language to start:",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Language selection
async def lang_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data
    if lang == "lang_en":
        context.user_data['lang'] = "en"
        await show_menu_en(query)
    elif lang == "lang_bn":
        context.user_data['lang'] = "bn"
        await show_menu_bn(query)

# Main Menu EN
async def show_menu_en(query):
    keyboard = [
        [InlineKeyboardButton("👤 Profile", callback_data='profile_en')],
        [InlineKeyboardButton("💼 Projects", callback_data='projects_en')],
        [InlineKeyboardButton("✉️ Contact", callback_data='contact_en')],
        [InlineKeyboardButton("🌐 Website", url="https://example.com")],
        [InlineKeyboardButton("🔒 Privacy Policy", url="https://example.com/privacy")],
        [InlineKeyboardButton("⚡ Powered by Swygen", url="https://t.me/swygenofficial")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="✨ **Main Menu \English\**\n\nPlease choose an option below:",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Main Menu BN
async def show_menu_bn(query):
    keyboard = [
        [InlineKeyboardButton("👤 প্রোফাইল", callback_data='profile_bn')],
        [InlineKeyboardButton("💼 প্রজেক্টসমূহ", callback_data='projects_bn')],
        [InlineKeyboardButton("✉️ যোগাযোগ", callback_data='contact_bn')],
        [InlineKeyboardButton("🌐 ওয়েবসাইট", url="https://example.com")],
        [InlineKeyboardButton("🔒 গোপনীয়তা নীতি", url="https://example.com/privacy")],
        [InlineKeyboardButton("⚡ Powered by Swygen", url="https://t.me/swygenofficial")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="✨ **মেইন মেনু \বাংলা\**\n\nনিচের অপশন থেকে বেছে নিন:",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Profile EN
async def profile_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 Back", callback_data='lang_en')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_media(
        media=InputMediaPhoto(
            media="https://assets.onecompiler.app/43ea4pg72/43ejdw4bt/Grey%20Yellow%20Minimalist%20Software%20Development%20Logo.png",  # তোমার প্রোফাইল Photo
            caption="👤 **About Me**\n\n"
                    "• Name: **Ayman Hasan Shaan**\n"
                    "• Skills: Python \\| Telegram Bots \\| Web Developer\n"
                    "• Experience: 3+ Years\n\n"
                    "⚡ **Bringing ideas into reality\\!**\n\n"
                    "🌐 **Social Links**:\n"
                    "• Instagram: [@swygenofficial](https://instagram.com/swygenofficial)\n"
                    "• GitHub: [Swygen GitHub](https://github.com/swygen-bd-dev)\n"
                    "• WhatsApp: [Chat with me](https://wa.me/message/BQ77IMY2MHW6E1)\n"
                    "• Facebook: [My Facebook](https://facebook.com/ayman.hasan.shaan)\n",
            parse_mode='MarkdownV2'
        ),
        reply_markup=reply_markup
    )

# Profile BN
async def profile_bn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 ফিরে যান", callback_data='lang_bn')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_media(
        media=InputMediaPhoto(
            media="https://telegra.ph/file/8c7c3c5a9b27ea915d1b1.jpg",
            caption="👤 **আমার সম্পর্কে**\n\n"
                    "• নাম: **আয়মান হাসান শান**\n"
                    "• দক্ষতা: পাইথন \\| টেলিগ্রাম বট \\| ওয়েব ডেভেলপার\n"
                    "• অভিজ্ঞতা: ৩+ বছর\n\n"
                    "⚡ **আপনার আইডিয়াকে বাস্তবে রূপ দিই\\!**\n\n"
                    "🌐 **সোশ্যাল লিঙ্ক**:\n"
                    "• Instagram: [@swygenofficial](https://instagram.com/swygenofficial)\n"
                    "• GitHub: [Swygen GitHub](https://github.com/swygen-bd-dev)\n"
                    "• WhatsApp: [আমার সাথে কথা বলুন](https://wa.me/message/BQ77IMY2MHW6E1)\n"
                    "• Facebook: [আমার Facebook](https://facebook.com/ayman.hasan.shaan)\n",
            parse_mode='MarkdownV2'
        ),
        reply_markup=reply_markup
    )

# Projects EN
async def projects_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 Back", callback_data='lang_en')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="💼 **Projects**\n\n• Premium Telegram Bots\n• Full Stack Web Development\n• API Integration & Automation",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Projects BN
async def projects_bn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 ফিরে যান", callback_data='lang_bn')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="💼 **প্রজেক্টসমূহ**\n\n• প্রিমিয়াম টেলিগ্রাম বট\n• ফুল স্ট্যাক ওয়েব ডেভেলপমেন্ট\n• এপিআই ইন্টিগ্রেশন ও অটোমেশন",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Contact EN
async def contact_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 Back", callback_data='lang_en')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="✉️ **Contact Info**\n\nEmail: swygenofficial@gmail.com\nTelegram: @swygenofficial",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Contact BN
async def contact_bn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardButton("🔙 ফিরে যান", callback_data='lang_bn')
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="✉️ **যোগাযোগ করুন**\n\nইমেইল: swygenofficial@gmail.com\nটেলিগ্রাম: @swygenofficial",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

def main():
    app = ApplicationBuilder().token('7870153726:AAHNAJWQpMhk2UXe1iXwWBiNC59ojAMnbO8').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(lang_select, pattern='^lang_'))
    app.add_handler(CallbackQueryHandler(profile_en, pattern='^profile_en$'))
    app.add_handler(CallbackQueryHandler(profile_bn, pattern='^profile_bn$'))
    app.add_handler(CallbackQueryHandler(projects_en, pattern='^projects_en$'))
    app.add_handler(CallbackQueryHandler(projects_bn, pattern='^projects_bn$'))
    app.add_handler(CallbackQueryHandler(contact_en, pattern='^contact_en$'))
    app.add_handler(CallbackQueryHandler(contact_bn, pattern='^contact_bn$'))

    app.run_polling()

if __name__ == '__main__':
    main()
