import os
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WHATSAPP_FROM = "whatsapp:+14155238886"  # Número de Twilio
WHATSAPP_TO = os.getenv("WHATSAPP_TO")   # Número de destino

