import json
from types import SimpleNamespace

data = '''[{"name": "John Smith", "hometown": {"name": "New York", "id": 123}},
{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}]'''

# Parse JSON into an object with attributes corresponding to dict keys.
with open("Pytho") as f:
    file = json.load(f)
    print(file)
# x = json.load(, object_hook=lambda d: SimpleNamespace(**d))
# print(x)

# for elem in x:
#     print(elem.name, elem.hometown.name, elem.hometown.id)