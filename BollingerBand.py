import numpy as np


    
price = [1145.2, 1150.15, 1152.9, 1152.8, 1153.6, 
         1155.35, 1153.75, 1150.3, 1146.85, 1147.2, 
         1149.75, 1148.1, 1147.6, 1150.95, 1153.55, 
         1154.3, 1157.25, 1161.15, 1160.5, 1164.25,]
    


def calculate_bollinger_bands(price_list, window=20, num_std_dev=2):

    """Calculates Upper Band, Middle Band (SMA), and Lower Band."""
    if len(price_list) < window:
        return None, None, None  # Not enough data

    middle_band = np.mean(price_list)  # Simple Moving Average
    std_dev = np.std(price_list)  # Standard Deviation

    upper_band = middle_band + (num_std_dev * std_dev)
    lower_band = middle_band - (num_std_dev * std_dev)

    return upper_band, middle_band, lower_band

def update_price(GetNewValue=None):

    global price
    
    
    if GetNewValue:
        print('GetNewValue')
        price.pop(0)
        price.append(GetNewValue)
        print(price)
        
    upper, middle, lower = calculate_bollinger_bands(price)

    Upper_Band = f"{upper:.2f}"
    Middle_Band = f"{middle:.2f}"
    Lower_Band = f"{lower:.2f}"

   
    return Upper_Band, Middle_Band, Lower_Band

    

    

# ✅ Example usage: 
print(update_price())