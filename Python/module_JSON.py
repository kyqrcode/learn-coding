import json

#python dictionary to JSON format
#aka encoding or serialization
fileName = {"name": "John", "age": 30, "city": "New York", "hasChildren": False}
fileJSON = json.dumps(fileName, indent=4, separators='; ', sort_keys=True)

with open('module_JSON.json', 'w') as file:
	json.dump(fileName, file)