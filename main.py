import requests
import schedule
import time

TOKEN = '7644929990:AAF83vap5-Tx_5174fB_kpxyqrIPvkZ6g9Q'
CHAT_ID = '1884452224'

def get_news():
    return 'Останні новини: https://news.google.com/search?q=контрабанда+Румунія+Угорщина&hl=uk'

def send_message():
    text = get_news()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=data)

schedule.every().day.at("05:30").do(send_message)  # Railway = UTC, 05:30 = 08:30 Київ

while True:
    schedule.run_pending()
    time.sleep(60)
