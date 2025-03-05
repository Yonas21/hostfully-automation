import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')
AGENCY_UID = os.getenv('AGENCY_UID')
AGENCY_API_KEY = os.getenv('AGENCY_API_KEY')
PROPERTY_ID = os.getenv('PROPERTY_ID')
LEAD_UID = os.getenv('LEAD_UID')