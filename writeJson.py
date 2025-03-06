import json

def writeToJson(json_data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
