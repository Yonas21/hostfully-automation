import requests
from config import API_URL, AGENCY_UID
from headers import headers

def get_agencies(AGENCY_URL, headers):
    response  = requests.get(AGENCY_URL+ "/agencies", headers=headers)
    return response.json()


def get_agency_by_id(AGENCY_URL, headers, agency_id):
    response = requests.get(AGENCY_URL + "/agencies/" + agency_id, headers=headers)
    return response.json()

print(get_agencies(API_URL, headers))
print(get_agency_by_id(API_URL, headers, AGENCY_UID))