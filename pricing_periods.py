import requests
from config import API_URL, LEAD_UID, PROPERTY_ID
from headers import headers


def get_pricing_periods(api_url, headers, property_id, start_date, end_date):
    if property_id:
        response = requests.get(
            f"{api_url}/pricing-periods?propertyUid={property_id}&from={start_date}&to={end_date}", headers=headers
        )
        return response.json()
    else:
        return None

start_date = "2015-01-01"
end_date = "2025-11-01"
pricing_periods = get_pricing_periods(API_URL, headers, PROPERTY_ID, start_date, end_date)
print("pricing period: ", pricing_periods)