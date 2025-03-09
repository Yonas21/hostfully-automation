import requests
from config import API_URL, AGENCY_UID
from headers import headers

def get_service_providers(api_url, headers, agency_uid):
    response = requests.get(
        f"{api_url}/service-providers?agencyUid={agency_uid}",
        headers=headers,
    )
    return response.json()

def get_service_providers_by_id(api_url, headers, service_provider_id):
    response = requests.get(
        f"{api_url}/service-providers/{service_provider_id}",
        headers=headers,
    )
    return response.json()

service_providers = get_service_providers(API_URL, headers, AGENCY_UID)
print("service_providers: ", service_providers)
