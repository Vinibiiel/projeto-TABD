import re
import json

def clean_string(string):
    new_string = string.strip()
    return new_string.strip("'")

def parse_insert_sql(file_path):
    with open(file_path, 'r') as file:
        sql_statements = file.read()

    insert_pattern = re.compile(r"insert into (\w+)\s*values\s*\((.*?)\);", re.IGNORECASE)
    matches = insert_pattern.findall(sql_statements)
    extracted_data = []

    for match in matches:
        table_name = match[0]
        values = match[1].split(',')

        formatted_values = [clean_string(v) for v in values]

        data_entry = {
            "table_name": table_name,
            "data": formatted_values
        }

        extracted_data.append(data_entry)

    with open('./data/data.json', 'w') as json_file:
        json.dump(extracted_data, json_file, indent=2)

file_path = 'largeRelationsInsertFile.sql'
parse_insert_sql(file_path)
