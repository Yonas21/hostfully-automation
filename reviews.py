import requests 
from config import API_URL, PROPERTY_ID, LEAD_UID
from headers import headers

def get_reviews(api_url, headers, property_id=None, lead_id=None, updatedSince = None):
    if property_id:
        if updatedSince is None:
            response = requests.get(f"{api_url}/reviews?propertyUid={property_id}", headers=headers)
            return response.json()
        else:
            response = requests.get(
                f"{api_url}/reviews?propertyUid={property_id}&updatedSince={updatedSince}",
                headers=headers,
            )
            return response.json()

    elif lead_id:
        if updatedSince is None:
            response = requests.get(f"{api_url}/reviews?leadUid={lead_id}", headers=headers)
            return response.json()
        else:
            response = requests.get(
                f"{api_url}/reviews?leadUid={lead_id}&updatedSince={updatedSince}",
                headers=headers,
            )
            return response.json()

    else:
        return None

def get_review_by_id(api_url, headers, review_id):
    response = requests.get(
        f"{api_url}/reviews/{review_id}",
        headers=headers,
    )
    return response.json()

reviews = get_reviews(API_URL, headers, PROPERTY_ID)
print("Reviews: ", reviews)
