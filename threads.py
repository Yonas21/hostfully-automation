import requests
from config import API_URL, AGENCY_UID, LEAD_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson


# get threads
def get_threads(API_URL, headers, AGENCY_UID, LEAD_UID):
    response = requests.get(
        API_URL + "/threads?agencyUid=" + AGENCY_UID + "&leadUid=" + LEAD_UID,
        headers=headers,
    )
    return response.json()


threads = get_threads(API_URL, headers, AGENCY_UID, LEAD_UID)
print("threads: ", threads)


csv_file_path = "./output/threads.csv"  # TODO: change this to a relative path

write_output_to_csv(threads, "threads", csv_file_path)

print(f"Guests data has been written to {csv_file_path}")

json_file_path = "./output/threads.json"
writeToJson(threads, json_file_path)
print(f"threads data has been written to {csv_file_path} and {json_file_path}")
