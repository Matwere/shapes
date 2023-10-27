import json
import os

def merge_json_files(file1, file2):
    try:
        # Load data from the first JSON file
        with open(file1, 'r') as f1:
            data1 = json.load(f1)

        # Load data from the second JSON file
        with open(file2, 'r') as f2:
            data2 = json.load(f2)

        # Merge the two JSON objects
        merged_data = {**data1, **data2}

        # Define the output directory and filename
        output_dir = '/Users/john_doe/output/'
        output_filename = 'merged_output.json'
        output_path = os.path.join(output_dir, output_filename)

        # Save the merged data to the output directory
        with open(output_path, 'w') as output_file:
            json.dump(merged_data, output_file, indent=4)

        print(f'Merged data saved to {output_path}')

    except FileNotFoundError:
        print('One or both input files not found.')
    except json.JSONDecodeError:
        print('Error decoding JSON data in one or both files.')

if __name__ == "__main__":
    # Specify the paths to the two JSON files
    file1 = '/Users/john_doe/envs/file1.json'
    file2 = '/Users/john_doe/envs/file2.json'

    # Call the merge_json_files function
    merge_json_files(file1, file2)
