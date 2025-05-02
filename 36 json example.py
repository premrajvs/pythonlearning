# Scenario: Loading JSON data from a string.
import json
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data["name"])

# Scenario: Dumping Python dictionary to a JSON string.
python_dict = {"title": "Python Basics", "pages": 200}
json_output = json.dumps(python_dict, indent=4)
print(json_output)