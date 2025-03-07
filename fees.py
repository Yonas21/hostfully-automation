import requests
from config import API_URL, PROPERTY_ID
from headers import headers


def get_fees(api_url, property_id):
    response = requests.get(f"{api_url}/fees/{property_id}", headers=headers)
    return response.json()

def get_fee_details(api_url, fee_id):
    response = requests.get(f"{api_url}/fees/{fee_id}", headers=headers)
    return response.json()


fees_information = get_fees(API_URL, PROPERTY_ID)
print("fees: ", fees_information)

# commented because there is no employee information for the time being used
# fee_id = fees_information.get("fees", [])[0]['uid']
# print("fee id: ", fee_id)