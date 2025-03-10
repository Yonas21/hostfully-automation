import requests
from config import API_URL, AGENCY_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


def get_agencies(api_url, headers):
    try:
        response = requests.get(f"{api_url}/agencies", headers=headers)
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


def get_agency_by_id(api_url, headers, agency_id):
    try:
        response = requests.get(f"{api_url}/agencies/{agency_id}" + agency_id, headers=headers)
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

agencies_informations = get_agencies(API_URL, headers)
if agencies_informations:
    print(agencies_informations)

    csv_file_path = "./output/agencies.csv"  # will be created if it doesn't exist

    write_output_to_csv(agencies_informations, "agencies", csv_file_path)
    print(f"Agencies data has been written to {csv_file_path}")

    json_file_path = "./output/agencies.json"
    writeToJson(agencies_informations, json_file_path)
    print(f"Agencies data has been written to {csv_file_path} and {json_file_path}")
else:
    print("Failed to retrieve agencies information.")
