#!/usr/bin/env python3.6

import json
import requests

data = {
    "president": {
        "name": "Ghazanfar Darko",
        "species": "GoldenMiner"
    }
}
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

print(json.dumps(data, indent=4)) # Serialization

with open('output_file.json', 'w') as write_file:
    json.dump(data, write_file) # Serialization


data = json.loads(json_string) # Deserialization
print(data)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text) # Deserialization
print(todos[0]['title'])
for i in todos:
    print(i['title'])