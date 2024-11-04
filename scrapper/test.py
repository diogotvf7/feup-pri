import json

def count_empty_stocks(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    count = 0
    for entry in data:
        if isinstance(entry, dict):  
            count += 1
    
    return count

if __name__ == "__main__":
    json_file_path = 'database/modified_data.json'  
    result = count_empty_stocks(json_file_path)
    print(f"Number of entries with 'stocks_changes_name' and 'stocks_changes_value' set to empty lists: {result}")
