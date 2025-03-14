import requests
from config import API_URL, AGENCY_UID, LEAD_UID, PROPERTY_ID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson
from properties import get_properties_by_id
import json
from datetime import datetime


# get messages
# GET /messages
# by changing the arguments agency_id, thread_id, lead_id and all of them are used separately and also you can apply pased by using date filter,limit and cursor too
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


# get individual message by id
# GET /messages/{message_id}
def get_message_by_id(api_url, headers, message_id):
    try:
        response = requests.get(f"{api_url}/messages/{message_id}", headers=headers)
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


def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        return dt.strftime("%B %d, %Y %I:%M %p")
    except Exception:
        return "Unknown Date"


# messages = get_messages(API_URL, headers, agency_id=AGENCY_UID, created_at="2019-01-01T00:00:00Z", limit=10)
each_property = get_properties_by_id(API_URL, headers, PROPERTY_ID)
# print("each_property: ", each_property)
messages = {"messages": [
    {
      "uid": "string",
      "createdUtcDateTime": "2025-03-10T18:19:41.087Z",
      "status": "CREATED",
      "type": "HOSTFULLY_PMP",
      "senderType": "SYSTEM",
      "content": {
        "subject": "string",
        "text": "string"
      },
      "threadUid": "string",
      "attachments": [
        {
          "uid": "string",
          "uri": "string",
          "fileName": "string",
          "contentType": "string",
          "type": "IMAGE_JPEG"
        }
      ]
    },    {
      "uid": "string",
      "createdUtcDateTime": "2025-03-11T18:19:41.087Z",
      "status": "CREATED",
      "type": "HOSTFULLY_PMP",
      "senderType": "SYSTEM",
      "content": {
        "subject": "string",
        "text": "string"
      },
      "threadUid": "string",
      "attachments": [
        {
          "uid": "string",
          "uri": "string",
          "fileName": "string",
          "contentType": "string",
          "type": "IMAGE_JPEG"
        }
      ]
    },    {
      "uid": "string",
      "createdUtcDateTime": "2025-03-13T18:19:41.087Z",
      "status": "CREATED",
      "type": "HOSTFULLY_PMP",
      "senderType": "SYSTEM",
      "content": {
        "subject": "string",
        "text": "string"
      },
      "threadUid": "string",
      "attachments": [
        {
          "uid": "string",
          "uri": "string",
          "fileName": "string",
          "contentType": "string",
          "type": "IMAGE_JPEG"
        }
      ]
    },    {
      "uid": "string",
      "createdUtcDateTime": "2025-03-14T18:19:41.087Z",
      "status": "CREATED",
      "type": "HOSTFULLY_PMP",
      "senderType": "SYSTEM",
      "content": {
        "subject": "string",
        "text": "string"
      },
      "threadUid": "string",
      "attachments": [
        {
          "uid": "string",
          "uri": "string",
          "fileName": "string",
          "contentType": "string",
          "type": "IMAGE_JPEG"
        }
      ]
    },
  ],
  "_metadata": {
    "count": 0,
    "totalCount": 0
  },
  "_paging": {
    "_limit": 0,
    "_nextCursor": "string"
  }
}
property_name = each_property["property"]["name"]
for message in messages["messages"]:
    message["properyName"] = property_name
    message["hostfullID"] = AGENCY_UID

# print(json.dumps(messages, indent=4))
filtered_messages = {"messages":[
    {
        "propertyName": message.get(
            "properyName", "Unknown Property"
        ),  # Handle misspelled key
        "createdDate": format_date(message.get("createdUtcDateTime", "Unknown Date")),
        "hostfullID": message.get("hostfullID", "Unknown ID"),
        "text": message.get("content", {}).get("text", "No Text"),
    }
    for message in messages.get("messages", [])
]}
# print("messages at first: ", messages)
if filtered_messages:
    print(json.dumps(filtered_messages, indent=4))

    csv_file_path = "./output/messages.csv"  # TODO: change this to a relative path
    write_output_to_csv(filtered_messages, "messages", csv_file_path)
    print(f"Messages data has been written to {csv_file_path}")

    json_file_path = "./output/messages.json"
    writeToJson(filtered_messages, json_file_path)
    print(f"Messages data has been written to {csv_file_path} and {json_file_path}")
else:
    print("No messages found.")
