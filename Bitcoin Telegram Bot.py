import requests
import time
api_key='fdaksnal-smka-4klms-8klmsa-f9slamlas8'#Get your  api_key from https://coinmarketcap.com/api 
bot_key='529895665:AAF8GKddjksndlsnkldkldnkdal'#Get your  bot_key from BotFather on Telegram
chat_id='864654688' #Get your chat_id from IDBot on Telegram  
limit=30000
time_interval=5*60

def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start':'1',
        'limit':'10',
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    
    response=requests.get(url,headers=headers).json()
    btc_price=response['data'][0]['quote']['USD']['price']
    
    return  btc_price

def send_update(chat_id,msg):
    url=f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price=get_price()
        if price <limit:   
           send_update(chat_id,f"Bitcoin last price is :{price}")
        time.sleep(time_interval)
main()
