import requests
from config import API_URL
from headers import headers

def get_units(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/multi-units/units?unitTypeUid={property_id}", headers
    )
    return response.json()

def get_unit_by_id(api_url, headers, unit_id):
    response = requests.get(
        f"{api_url}/multi-units/units/{unit_id}", headers
    )
    return response.json()