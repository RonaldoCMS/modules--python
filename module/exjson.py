import json

x = '{"name":"Fabio", "surname":"Ronaldo"}'
y = json.loads(x)

print(y["name"])