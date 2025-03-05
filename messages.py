import requests
from config import API_URL, AGENCY_UID, LEAD_UID
from headers import headers


#get messages
#TODO: implement multiple arguments
def get_messages(API_URL, headers, AGENCY_UID, LEAD_UID):
    response  = requests.get(API_URL+ "/messages?agencyUid="+AGENCY_UID+"&leadUid="+LEAD_UID, headers=headers)
    return response.json()


print(get_messages(API_URL, headers,AGENCY_UID, LEAD_UID))
