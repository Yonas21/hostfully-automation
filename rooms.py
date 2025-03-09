import requests
from config import API_URL, PROPERTY_ID
from headers import headers


def get_rooms(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/rooms?propertyUid={property_id}",
        headers=headers,
    )
    return response.json()

def get_room_by_id(api_url,headers,room_id):
    response = requests.get(
        f"{api_url}/rooms/{room_id}",
        headers=headers,
    )
    return response.json()

rooms = get_rooms(API_URL, headers, PROPERTY_ID)
print("rooms: ", rooms)
