import requests
from config import API_URL, PROPERTY_ID
from headers import headers


def get_local_spots(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/local-spots?propertyUid={property_id}", headers=headers
    )
    return response.json()

def local_spot_by_id(api_url, headers, local_spot_id):
    response = requests.get(f"{api_url}/local-spots/{local_spot_id}", headers=headers)
    return response.json()


local_spots = get_local_spots(API_URL, headers, PROPERTY_ID)
print ("local_spots", local_spots)
