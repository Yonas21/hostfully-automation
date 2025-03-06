import requests
from config import API_URL, AGENCY_UID, LEAD_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


# get messages
# TODO: implement multiple arguments
def get_messages(API_URL, headers, AGENCY_UID, LEAD_UID):
    response  = requests.get(API_URL+ "/messages?agencyUid="+AGENCY_UID+"&leadUid="+LEAD_UID, headers=headers)
    return response.json()


messages = get_messages(API_URL, headers,AGENCY_UID, LEAD_UID)
print("messages: " , messages)

csv_file_path = "./output/messages.csv"  # TODO: change this to a relative path

write_output_to_csv(messages, "messages", csv_file_path)

print(f"Guests data has been written to {csv_file_path}")

json_file_path = "./output/messages.json"
writeToJson(messages, json_file_path)
print(f"messages data has been written to {csv_file_path} and {json_file_path}")
