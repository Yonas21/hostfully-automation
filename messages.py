import requests
from config import API_URL, AGENCY_UID, LEAD_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


# get messages
# TODO: implement multiple arguments
def get_messages(api_url, headers, agency_id=None, thread_id=None, lead_id=None, created_at=None, limit=None, cursor=None):
    params = {}
    if agency_id:
        params['agencyUid'] = agency_id
    if thread_id:
        params['threadUid'] = thread_id
    if lead_id:
        params['leadUid'] = lead_id
    if created_at:
        params['createdAt'] = created_at
    if limit:
        params['limit'] = limit
    if cursor:
        params['cursor'] = cursor

    try:
        response = requests.get(f"{api_url}/messages", headers=headers, params=params)
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


messages = get_messages(API_URL, headers, agency_id=AGENCY_UID, created_at="2025-01-01T00:00:00Z", limit=10)

print("messages at first: ", messages)
if messages:
    print("messages: ", messages)

    csv_file_path = "./output/messages.csv"  # TODO: change this to a relative path
    write_output_to_csv(messages, "messages", csv_file_path)
    print(f"Messages data has been written to {csv_file_path}")

    json_file_path = "./output/messages.json"
    writeToJson(messages, json_file_path)
    print(f"Messages data has been written to {csv_file_path} and {json_file_path}")
else:
    print("No messages found.")
