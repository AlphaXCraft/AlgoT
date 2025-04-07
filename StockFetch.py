import requests
from bs4 import BeautifulSoup

def Get_Fetch_Stock(
                             
    url: str = "https://www.google.com/finance/quote/RELIANCE:NSE",
    class_name: str = "YMlKec fxKbKc") -> float:

    # url = "https://www.google.com/finance/quote/RELIANCE:NSE"
    # class_name = "YMlKec fxKbKc"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('div', class_=class_name)

        if price_element:
            # Remove ₹ and commas, then convert to float
            raw_text = price_element.text.strip().replace('₹', '').replace(',', '')
            return float(raw_text)
        else:
            print("Price element not found. The class name may be incorrect or has changed.")
            return -1.0

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return -1.0

# Example usage
# price = Get_Fetch_Stock()
# print(price)

# while True:
#     print(Get_Fetch_Stock())
#     print(Get_Fetch_Stock('https://www.google.com/finance/quote/HDFCBANK:NSE'))
#     print('-------------')

print(Get_Fetch_Stock())