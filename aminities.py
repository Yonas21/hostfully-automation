import requests
from config import API_URL, PROPERTY_ID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson

# current aminities assigned for the property
def get_aminities(API_URL, headers, PROPERTY_ID):
    response  = requests.get(API_URL+ "/amenities"+"?propertyUid="+PROPERTY_ID, headers=headers)
    return response.json()


# get unique aminities by aminity id
def get_aminites_by_id(AGENCY_URL, headers, Aminity_ID):
    response = requests.get(AGENCY_URL + "/amenities/" + Aminity_ID, headers=headers)
    return response.json()


# available aminities for the property
def get_available_aminities(API_URL, headers, PROPERTY_ID):
    response = requests.get(API_URL + "/available-amenities"+"?propertyUid="+PROPERTY_ID, headers=headers)
    return response.json()


def get_available_property_rules(API_URL, headers, PROPERTY_ID):
    response = requests.get(API_URL + "/available-property-rules"+"?propertyUid="+PROPERTY_ID, headers=headers)
    return response.json()


def get_custom_amenities(API_URL, headers, PROPERTY_ID):
    response = requests.get(API_URL + "/custom-amenities"+"?objectUid="+PROPERTY_ID+"&objectType=PROPERTY", headers=headers)
    return response.json()

# call and test functions

aminities_information = get_aminities(API_URL, headers, PROPERTY_ID=PROPERTY_ID)
print("aminities: ", aminities_information)

csv_file_path = "./output/amenities.csv"  # TODO: change this to a relative path

write_output_to_csv(aminities_information, "amenities", csv_file_path)

print(f"Guests data has been written to {csv_file_path}")

json_file_path = "./output/amenities.json"
writeToJson(aminities_information, json_file_path)
print(f"amenities data has been written to {csv_file_path} and {json_file_path}")


# print("unique aminity: ", get_aminites_by_id(API_URL, headers, "ced22978-d679-4359-b1c2-ab53db36e5fc"))
# print("available aminities: ", get_available_aminities(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
# print("available property rules: ", get_available_property_rules(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
# print("custom aminities: ", get_custom_amenities(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
