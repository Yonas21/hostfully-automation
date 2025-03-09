import requests
from config import API_URL, PROPERTY_ID
from headers import headers

def get_property_rules(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/property-rules?propertyUid={property_id}",
        headers=headers,
    )
    return response.json()

def get_property_rules_by_id(api_url, headers, rule_id):
    response = requests.get(
        f"{api_url}/property-rules/{rule_id}",
        headers=headers,
    )
    return response.json()

property_rules = get_property_rules(API_URL, headers, PROPERTY_ID)
print("property_rules: ", property_rules)