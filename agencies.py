import requests
from config import API_URL, AGENCY_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


def get_agencies(AGENCY_URL, headers):
    response  = requests.get(AGENCY_URL+ "/agencies", headers=headers)
    return response.json()


def get_agency_by_id(AGENCY_URL, headers, agency_id):
    response = requests.get(AGENCY_URL + "/agencies/" + agency_id, headers=headers)
    return response.json()

agencies_informations = get_agencies(API_URL, headers)
print(agencies_informations)

csv_file_path = "./output/agencies.csv"  # TODO: change this to a relative path

write_output_to_csv(agencies_informations, csv_file_path)

print(f"Guests data has been written to {csv_file_path}")

json_file_path = "./output/agencies.json"
writeToJson(agencies_informations, json_file_path)
print(f"Agencies data has been written to {csv_file_path} and {json_file_path}")
