import requests
from config import API_URL, PROPERTY_ID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


# get all booking information for specific agency and property by id
# GET /leads
# GET /leads?propertyUid={property_id}
# GET /leads?agencyUid={agency_id}
def get_leads(
    api_url,
    headers,
    property_id=None,
    agency_id=None,
    checkInFrom=None,
    checkOutFrom=None,
    checkInTo=None,
    checkOutTo=None,
    limit=None,
    cursor=None,
    updatedSince=None,
):
    try:
        params = {}
        if property_id:
            params['propertyUid'] = property_id
        if agency_id:
            params['agencyUid'] = agency_id
        if checkInFrom:
            params['checkInFrom'] = checkInFrom
        if checkOutFrom:
            params['checkOutFrom'] = checkOutFrom
        if checkInTo:
            params['checkInTo'] = checkInTo
        if checkOutTo:
            params['checkOutTo'] = checkOutTo
        if limit:
            params['limit'] = limit
        if cursor:
            params['cursor'] = cursor
        if updatedSince:
            params['updatedSince'] = updatedSince

        response = requests.get(f"{api_url}/leads", headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
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


# get all booking information by id
# GET /leads/{lead_id}
def lead_by_id(api_url, headers, lead_id):
    try:
        response = requests.get(
                f"{api_url}/leads/{lead_id}", headers=headers
            )
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


leads = get_leads(API_URL, headers, PROPERTY_ID, updatedSince="2019-01-01T00:00:00Z", limit=10)
print("leads: ", leads)

if leads:
    print("leads: ", leads)

    csv_file_path = "./output/leads.csv"  # TODO: change this to a relative path
    write_output_to_csv(leads, "leads", csv_file_path)
    print(f"leads data has been written to {csv_file_path}")

    json_file_path = "./output/leads.json"
    writeToJson(leads, json_file_path)
    print(f"leads data has been written to {csv_file_path} and {json_file_path}")
else:
    print("No leads found.")
