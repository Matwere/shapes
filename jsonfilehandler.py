import json


def read_jsonDictionary(FILEPATH: str):
    shape_coordinates = []

    try:
        with open(FILEPATH, 'r') as file:
            for line in file:
                data = json.loads(line)
                if "coordinates" in data:
                    shape_coordinates.append(data["coordinates"])
                    # If you want to extract other information, modify this line accordingly

    except FileNotFoundError:
        print(f"File {FILEPATH} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {FILEPATH}.")

    return shape_coordinates

# Example usage:
# Replace 'your_file_path.json' with the actual file path
shapes = read_jsonline('your_file_path.json')
print(shapes)
