import requests
from config import API_URL, AGENCY_UID
from headers import headers


def get_employees(api_url, agency_id):
    response = requests.get(f"{api_url}/employees?agencyUid={agency_id}", headers=headers)
    return response.json()


def get_employee_by_id(api_url, employee_id):
    response = requests.get(f"{api_url}/employees/{employee_id}", headers=headers)
    return response.json()

employees_information = get_employees(API_URL, AGENCY_UID)
# print("Employees information: ",employees_information)

employee_id = employees_information.get("employees", [])[0]['uid']
print("Employee id: ", employee_id)
employee = get_employee_by_id(API_URL, employee_id)
print("Employee by id: ", employee)
