import time

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
                stock_price = Get_Fetch_Stock()
                print(f"[15-Min Check] Reliance Industries Ltd Stock Price: {stock_price}")
                print(f"{hour:02d}-{minute:02d}-{second:02d}")
                return True
    return False


# Fetches stock price every minute at second == 55
def fetch_stock_every_minute():
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    if 9 <= hour < 15:
        if second == 59:
            stock_price = Get_Fetch_Stock()
            print(f"[1-Min Check] Reliance Industries Ltd Stock Price: {stock_price}")
            print(f"{hour:02d}-{minute:02d}-{second:02d}")
            return True
    return False

while True:
   
    time.sleep(1)