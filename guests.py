import requests
from config import API_URL, AGENCY_UID
from headers import headers

def get_guests(AGENCY_URL, headers, AGENCY_UID):
    response  = requests.get(AGENCY_URL+ "/guests/"+AGENCY_UID, headers=headers)
    return response.json()


guests_information = get_guests(API_URL, headers, AGENCY_UID)
print(guests_information)
