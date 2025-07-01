import requests

# Replace with your real bot token and chat ID
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
CHAT_ID = 'YOUR_CHAT_ID_HERE'

def send_telegram_message_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            message = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message[:4096],  # Telegram limit is 4096 chars
        'parse_mode': 'HTML'
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ Message sent!")
    else:
        print(f"❌ Failed to send message: {response.text}")

# Example usage
send_telegram_message_from_file("message.txt")
