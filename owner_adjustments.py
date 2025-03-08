import requests
from config import API_URL, PROPERTY_ID
from headers import headers


def get_owner_adjustments(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/owner-adjustments?propertyUid={property_id}", headers=headers
    )
    return response.json()

def get_owner_adjustments_by_id(api_url, headers, id):
    response = requests.get(f"{api_url}/owner-adjustments/{id}", headers=headers)
    return response.json()

owner_adjustments = get_owner_adjustments(API_URL, headers, PROPERTY_ID)
print("Owner Adjustments: ", owner_adjustments)