import requests
from config import API_URL, PROPERTY_ID, LEAD_UID, SAMPLE_GUEST_ID
from headers import headers


def get_orders(api_url, headers, guest_id=None, property_id=None, lead_id=None):
    if guest_id is not None:
        response = requests.get(
            f"{api_url}/orders?guestUid={guest_id}", headers=headers
        )
        return response.json()
    elif property_id is not None:
        response = requests.get(
            f"{api_url}/orders?propertyUid={property_id}", headers=headers
        )
        return response.json()
    elif lead_id is not None:
        response = requests.get(
            f"{api_url}/orders?leadUid={lead_id}", headers=headers
        )
        return response.json()
    else:
        return None
    
orders = get_orders(API_URL, headers, property_id=PROPERTY_ID)
print("orders: ", orders)
