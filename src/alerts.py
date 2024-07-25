from datetime import datetime, timedelta
from crypto_api import get_crypto_price
from whatsapp_api import send_whatsapp_message

INITIAL_PRICE = None
PRICE_LOG = []  # Lista para mantener un registro de precios con tiempo

def log_price(price):
    # Registrar el precio actual con el tiempo
    now = datetime.now()
    PRICE_LOG.append((now, price))

def calculate_percentage_change(current_price, initial_price):
    return ((current_price - initial_price) / initial_price) * 100

def generate_alert(price, message):
    send_whatsapp_message(f"Alerta: {message}, Precio: {price}")

def monitor_price():
    global INITIAL_PRICE
    current_price = get_crypto_price()
    log_price(current_price)
    
    if INITIAL_PRICE is None:
        INITIAL_PRICE = current_price
    
    # Calcular cambios porcentuales para alertas
    half_hour_ago = datetime.now() - timedelta(minutes=30)
    prices_half_hour_ago = [price for time, price in PRICE_LOG if time >= half_hour_ago]
    
    if prices_half_hour_ago:
        initial_price_half_hour = prices_half_hour_ago[0]
        percentage_change = calculate_percentage_change(current_price, initial_price_half_hour)
        
        if percentage_change <= -0.5:
            generate_alert(current_price, "Baja más del 0.5% en media hora. Considera vender")
        elif percentage_change >= 0.5:
            generate_alert(current_price, "Subida más del 0.5% en media hora. Considera comprar")

def monitor_initial_price():
    global INITIAL_PRICE
    current_price = get_crypto_price()
    if INITIAL_PRICE is None:
        INITIAL_PRICE = current_price

