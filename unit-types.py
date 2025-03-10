import requests
from config import API_URL, SAMPLE_ORDER
from headers import headers

def get_unit_types(api_url, headers, hotel_id, updated_since):
    if updated_since:
        response = requests.get(
            f"{api_url}/unit-types?hotelUid={hotel_id}&updatedSince={updated_since}",
            headers=headers,
        )
        return response.json()
    else: 
        response = requests.get(
            f"{api_url}/unit-types?hotelUid={hotel_id}", headers=headers
        )
        return response.json()

def get_unit_type_by_id(api_url, headers, unit_type_id):
    response = requests.get(
        f"{api_url}/unit-types/{unit_type_id}", headers=headers
    )
    return response.json()
