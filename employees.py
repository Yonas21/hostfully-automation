import requests
from config import API_URL, AGENCY_UID
from headers import headers
from writecsv import write_output_to_csv
from writeJson import writeToJson

def get_employees(api_url, agency_id):
    try:
        response = requests.get(f"{api_url}/employees?agencyUid={agency_id}", headers=headers)
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

def get_employee_by_id(api_url, employee_id):
    try:
        response = requests.get(f"{api_url}/employees/{employee_id}", headers=headers)
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

employees_information = get_employees(API_URL, AGENCY_UID)
if employees_information:
    print("Employees information: ",employees_information)

    csv_file_path = "./output/employees.csv"
    write_output_to_csv(employees_information, "employees", csv_file_path)
    print(f"Employee data has been written to {csv_file_path}")

    json_file_path = "./output/employees.json"
    writeToJson(employees_information, json_file_path)
    print(f"Employee data has been written to {csv_file_path} and {json_file_path}")
else:
    print("Failed to retrieve custom information.")

employee_id = employees_information.get("employees", [])[0]['uid']
print("Employee id: ", employee_id)
employee = get_employee_by_id(API_URL, employee_id)
print("Employee by id: ", employee)
