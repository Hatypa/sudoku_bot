from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main():
    application = Application.builder().token(settings.API_KEY).build()

    logging.info('Starting')

    application.add_handler(CommandHandler('start', start))
    
    application.add_handler(MessageHandler(filters.TEXT, talk_to_me))


 
    application.run_polling(allowed_updates=Update.ALL_TYPES)

main()