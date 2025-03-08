import requests
from config import API_URL, PROPERTY_ID
from headers import headers


def get_leads(api_url, headers, property_id=None, agency_id=None):
    if property_id:
        response = requests.get(
            f"{api_url}/leads?propertyUid={property_id}", headers=headers
        )
        return response.json()
    elif agency_id:
        response = requests.get(
            f"{api_url}/leads?agencyUid={property_id}", headers=headers
        )
        return response.json()
    else:
        return None


def lead_by_id(api_url, headers, lead_id):
    response = requests.get(
            f"{api_url}/leads/{lead_id}", headers=headers
        )
    return response.json()

leads = get_leads(API_URL, PROPERTY_ID, headers)
print("leads: ", leads)
