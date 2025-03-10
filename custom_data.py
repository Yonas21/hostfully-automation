import requests
from config import API_URL, PROPERTY_ID, LEAD_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


def get_custom_data(api_url, headers, propery_uid=None, lead_uid=None):
    try:
        if propery_uid:
            response = requests.get(f"{api_url}/custom-data?propertyUid={propery_uid}", headers=headers)
            response.raise_for_status()
            return response.json()
        elif lead_uid:
            response = requests.get(f"{api_url}/custom-data?leadUid={lead_uid}", headers=headers)
            response.raise_for_status()
            return response.json()
        else:
            return None
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

# custom_data = get_custom_data(API_URL, headers, lead_uid=LEAD_UID)
# print("lead custom_data: " , custom_data)


custom_data = get_custom_data(API_URL, headers, PROPERTY_ID)
if custom_data:
    print("Custom Data: ", custom_data)

    csv_file_path = "./output/custom_data.csv"
    write_output_to_csv(custom_data, "custom_data", csv_file_path)
    print(f"Custom data has been written to {csv_file_path}")

    json_file_path = "./output/custom_data.json"
    writeToJson(custom_data, json_file_path)
    print(f"Custom data has been written to {csv_file_path} and {json_file_path}")
else:
    print("Failed to retrieve custom information.")
