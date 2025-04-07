import time

from BollingerBand import update_price
from StockFetch import Get_Fetch_Stock



# Fetches stock price every 15 minutes at second == 55
def fetch_stock_every_15_minutes():
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    if 9 <= hour < 15:
        if minute % 15 == 0:
            if second == 55:
                Stock_Price = Get_Fetch_Stock()
                Upper_Band, Middle_Band, Lower_Band = update_price(Stock_Price)
                
                print(f"{hour:02d}-{minute:02d}-{second:02d}")
                print(f"[15-Min Check] Reliance Industries Ltd Stock Price: {Stock_Price}")
                print(f'Upper Band:  {Upper_Band}')
                print(f'Middle Band: {Middle_Band}')
                print(f'Lower Band:  {Lower_Band}')

                return True
    else:
        print('Market Is Close.........')
            
    return False


# Fetches stock price every minute at second == 55
def fetch_stock_every_minute():
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    if 9 <= hour < 15:
        if second == 59:
            Stock_Price = Get_Fetch_Stock()
            print(f"[1-Min Check] Reliance Industries Ltd Stock Price: {Stock_Price}")
            print(f"{hour:02d}-{minute:02d}-{second:02d}")
            return True
        
    else:
        print('Market Is Close.........')
        
    return False

# while True:
   
#     time.sleep(1)

fetch_stock_every_15_minutes()
fetch_stock_every_minute()