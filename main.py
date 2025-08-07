import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import time
from dotenv import load_dotenv
load_dotenv()
from utils.checker import check_website_status
from utils.notifier import send_telegram_message
from utils.logger import log

load_dotenv()

URL = os.getenv("URL_TO_MONITOR")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL_SECONDS", 60))

def main():
    if not URL:
        log("❌ No se especificó una URL para monitorear. Agrega 'URL_TO_MONITOR' en tu .env")
        return

    print(f"📡 Monitoreando: {URL} cada {CHECK_INTERVAL} segundos.")
    
    while True:
        if check_website_status(URL):
            log(f"✅ {URL} está activa.")
        else:
            msg = f"🚨 {URL} parece estar caída."
            log(msg)
            send_telegram_message(msg)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
