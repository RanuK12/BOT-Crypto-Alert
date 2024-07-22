from crypto_api import get_crypto_price
from whatsapp_api import send_whatsapp_message

INITIAL_PRICE = None
THRESHOLDS = [1, 2, 3]  # Umbrales en porcentaje

def set_initial_price(crypto_id):
    global INITIAL_PRICE
    INITIAL_PRICE = get_crypto_price(crypto_id)
    print(f"Initial price set to {INITIAL_PRICE}")

def calculate_percentage_change(current_price, initial_price):
    return ((current_price - initial_price) / initial_price) * 100

def generate_alerts(crypto_id):
    global INITIAL_PRICE
    if INITIAL_PRICE is None:
        set_initial_price(crypto_id)
    
    current_price = get_crypto_price(crypto_id)
    change_percentage = calculate_percentage_change(current_price, INITIAL_PRICE)
    
    for threshold in THRESHOLDS:
        if change_percentage <= -threshold:
            send_whatsapp_message(f"Alerta de Compra: {crypto_id} ha bajado un {abs(change_percentage):.2f}% y ahora está en {current_price} USD")
        elif change_percentage >= threshold:
            send_whatsapp_message(f"Alerta de Venta: {crypto_id} ha subido un {change_percentage:.2f}% y ahora está en {current_price} USD")

if __name__ == "__main__":
    generate_alerts('bitcoin')
