# Configuraciones del bot

# Variables de entorno
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
TOKEN = os.getenv('TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
SUDO_IDS = [int(id) for id in os.getenv('SUDO_IDS').split(',')]

# Otras configuraciones personalizadas
# ...