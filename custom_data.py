import requests
from config import API_URL, PROPERTY_ID, LEAD_UID
from headers import headers


def get_custom_data(AGENCY_URL, headers, propery_uid = None, lead_uid = None):
    if propery_uid:
        response = requests.get(
            AGENCY_URL + "/custom-data?propertyUid=" + propery_uid, headers=headers
        )
        return response.json()
    elif lead_uid:
        response = requests.get(
            AGENCY_URL + "/custom-data?leadUid=" + lead_uid, headers=headers
        )
        return response.json()
    else:
        return None

custom_data = get_custom_data(API_URL, headers, PROPERTY_ID)
print("property custom_data: " , custom_data)
custom_data = get_custom_data(API_URL, headers, lead_uid=LEAD_UID)
print("lead custom_data: " , custom_data)
