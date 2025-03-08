import requests
import datetime
from config import API_URL, PROPERTY_ID
from headers import headers


def get_jobs(api_url, property_id, start_date, end_date, headers):
    response = requests.get(
        f"{api_url}/jobs?propertiesUids={property_id}&from={start_date}&to={end_date}",
        headers=headers,
    )
    return response.json()

def get_job_by_id(api_url, job_id):
    response = requests.get(
        f"{api_url}/jobs/{job_id}",
        headers=headers,
    )
    return response.json()


start_date = datetime.datetime.now().date().replace(month=1, day=1)
end_date = datetime.datetime.now().date().replace(month=12, day=31)
jobs = get_jobs(API_URL, PROPERTY_ID, start_date, end_date, headers)
print("jobs: ", jobs)
