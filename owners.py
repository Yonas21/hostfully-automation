import requests
from config import API_URL, AGENCY_UID
from headers import headers

def get_owners(api_url, headers, agency_id):
    response = requests.get(f"{api_url}/owners?agencyUid={agency_id}", headers=headers)
    return response.json()

def get_owner_by_id(api_url,headers,owner_id):
    response = requests.get(f"{api_url}/owners/{owner_id}", headers=headers)
    return response.json()

owners = get_owners(API_URL, headers, AGENCY_UID)
print("owners: ", owners)
