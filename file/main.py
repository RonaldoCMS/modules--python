import json

file = open("text.json", "r")
fileJson = json.loads(file.read())

print(fileJson["hobbies"][0])
