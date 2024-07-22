import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
WHATSAPP_FROM = os.getenv('WHATSAPP_FROM')
WHATSAPP_TO = os.getenv('WHATSAPP_TO')
COINGECKO_API_URL = os.getenv('COINGECKO_API_URL')

