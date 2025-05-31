from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import gbpusd_scaler  # Your main bot file

def start(update: Update, context: CallbackContext):
    update.message.reply_text('GBP/USD Scalper Bot Active! Use /signal to get latest trade signal.')

def get_signal(update: Update, context: CallbackContext):
    # You might want to modify your main() to return values instead of printing
    signal_info = gbpusd_scaler.main(return_values=True)
    update.message.reply_text(signal_info)

def main():
    creds = gbpusd_scaler.get_telegram_credentials()
    updater = Updater(token=creds['api_key'], use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("signal", get_signal))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
