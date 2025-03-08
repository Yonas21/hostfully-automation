import requests
from config import API_URL, PROPERTY_ID
from headers import headers

def get_photos(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/photos?propertyUid={property_id}", headers=headers
    )
    return response.json()

photos = get_photos(API_URL, headers, PROPERTY_ID)
print("photos: ", photos)