import requests
from config import API_URL, PROPERTY_ID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson

# current aminities assigned for the property
def get_aminities(api_url, headers, property_id):
    try:
        response = requests.get(f"{api_url}/amenities?propertyUid={property_id}", headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        return None


# get unique aminities by aminity id
def get_aminites_by_id(api_url, headers, amenity_id):
    try:
        response = requests.get(f"{api_url}/amenities/{amenity_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        return None


# available aminities for the property
def get_available_aminities(api_url, headers, property_id):
    try:
        response = requests.get(f"{api_url}/available-amenities?propertyUid={property_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        return None


def get_available_property_rules(api_url, headers, property_id):
    try:
        response = requests.get(f"{api_url}/available-property-rules?propertyUid={property_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        return None



def get_custom_amenities(api_url, headers, property_id):
    try:
        response = requests.get(f"{api_url}/custom-amenities?objectUid={property_id}&&objectType=PROPERTY", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        return None

# call and test functions

amenities_information = get_aminities(API_URL, headers, PROPERTY_ID)
if amenities_information:
    print("Amenities: ", amenities_information)

    csv_file_path = "./output/amenities.csv" 
    write_output_to_csv(amenities_information, "amenities", csv_file_path)
    print(f"Amenities data has been written to {csv_file_path}")

    json_file_path = "./output/amenities.json"
    writeToJson(amenities_information, json_file_path)
    print(f"Amenities data has been written to {csv_file_path} and {json_file_path}")
else:
    print("Failed to retrieve amenities information.")


# print("unique aminity: ", get_aminites_by_id(API_URL, headers, "ced22978-d679-4359-b1c2-ab53db36e5fc"))
# print("available aminities: ", get_available_aminities(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
# print("available property rules: ", get_available_property_rules(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
# print("custom aminities: ", get_custom_amenities(API_URL, headers, PROPERTY_ID=PROPERTY_ID))
