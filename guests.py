import requests
from config import API_URL, AGENCY_UID, LEAD_UID
from headers import headers

def get_guests(AGENCY_URL, headers, AGENCY_UID):
    response  = requests.get(AGENCY_URL+ "/guests/"+AGENCY_UID, headers=headers)
    return response.json()


def get_extra_guests(api_url, headers, lead_uid):
    response = requests.get(f"{api_url}/extra-guests/{lead_uid}", headers=headers)
    return response.json()

# guests_information = get_guests(API_URL, headers, AGENCY_UID)
# print(guests_information)


extra_guests = get_extra_guests(API_URL, headers, LEAD_UID)
print("extra_guests: ", extra_guests)
