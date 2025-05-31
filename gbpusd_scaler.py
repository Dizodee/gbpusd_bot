# Add these imports at the top
import requests
import configparser

# Add this function to read Telegram credentials
def get_telegram_credentials():
    config = configparser.ConfigParser()
    config.read('query.txt')
    return {
        'api_key': config['DEFAULT']['TELEGRAM_API_KEY'],
        'chat_id': config['DEFAULT']['TELEGRAM_CHAT_ID']
    }

# Add this function to send Telegram messages
def send_telegram_message(message):
    try:
        creds = get_telegram_credentials()
        url = f"https://api.telegram.org/bot{creds['api_key']}/sendMessage"
        params = {
            'chat_id': creds['chat_id'],
            'text': message
        }
        response = requests.post(url, params=params)
        return response.json()
    except Exception as e:
        print(f"⚠️ Telegram send error: {e}")
        return None

# Modify your main() function to send signals to Telegram
def main():
    show_branding()
    print("⚡ Initializing 15-Minute Scalping Engine...")
    
    # [Keep all your existing data loading and processing code]
    
    # After generating signal, add Telegram notification
    signal_message = (
        f"GBP/USD 15-Minute Scalper Alert\n"
        f"Time: {data.index[-1].strftime('%m/%d %H:%M')}\n"
        f"Price: {current_price:.5f}\n"
        f"Prediction: {predicted_price:.5f}\n"
        f"Change: {pct_change*100:.2f}%\n"
        f"Signal: {signal}"
    )
    
    print("\n📨 Sending Telegram notification...")
    send_telegram_message(signal_message)
