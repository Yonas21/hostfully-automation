import requests
from config import API_URL, PROPERTY_ID
from headers import headers

def get_cals(api_url, property_id, headers):
    response = requests.get(
        f"{api_url}/icals?propertyUid={property_id}", headers=headers
    )
    return response.json()

cals = get_cals(API_URL, PROPERTY_ID, headers)
print("cals: ", cals)
