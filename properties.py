import requests
from config import API_URL, AGENCY_UID, PROPERTY_ID
from headers import headers

def get_properties(api_url, headers, agency_id):
    response = requests.get(
        f"{api_url}/properties?agencyUid={agency_id}", headers=headers
    )
    return response.json()

def get_properties_by_id(api_url,headers, property_id):
    response = requests.get(
        f"{api_url}/properties/{property_id}", headers=headers
    )
    return response.json()


def get_property_calendars(api_url, headers, property_ids, start_date, end_date):
    response = requests.get(
        f"{api_url}/property-calendar?propertiesUids={property_ids}&from={start_date}&to={end_date}", headers=headers
    )
    return response.json()

def get_property_calendar(api_url, headers, property_id, start_date, end_date):
    response = requests.get(
        f"{api_url}/property-calendar/{property_id}?from={start_date}&to={end_date}",
        headers=headers,
    )
    return response.json()

def get_property_description(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/property-descriptions?propertyUid={property_id}",
        headers=headers,
    )
    return response.json()


def get_property_pricing_rules(api_url, headers, property_id):
    response = requests.get(
        f"{api_url}/property-pricing-rules/{property_id}",
        headers=headers,
    )
    return response.json()

# properties = get_properties(API_URL, headers, AGENCY_UID)
# print("properties: ", properties)

# start_date = "2015-01-01"
# end_date = "2016-01-01"
# each_property = get_properties_by_id(API_URL, headers, PROPERTY_ID)
# print("each_property: ", each_property)

# property_calendars = get_property_calendar(API_URL, headers,PROPERTY_ID, start_date, end_date)
# print("property_calendars: ", property_calendars)

# property_calendar = get_property_calendar(API_URL, headers,PROPERTY_ID, start_date, end_date)
# print("property_calendars: ", property_calendar)

# property_description = get_property_description(API_URL, headers, PROPERTY_ID)
# print("property_description: ", property_description)


# property_pricing_rules = get_property_pricing_rules(API_URL, headers, PROPERTY_ID)
# print("property_pricing_rules: ", property_pricing_rules)
