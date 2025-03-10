import os
import csv

def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
def write_output_to_csv(data, data_key, file_path):
    filtered_data = data.get(data_key, [])
    if filtered_data and len(filtered_data) > 0:
        headers = filtered_data[0].keys()
        directory_path = os.path.dirname(file_path)
        create_directory_if_not_exists(directory_path)
        with open(file_path, "w", newline="") as output_file:
            dict_writer = csv.DictWriter(output_file, headers)
            dict_writer.writeheader()
            dict_writer.writerows(filtered_data)
