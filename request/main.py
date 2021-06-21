import requests 

x = requests.get("http://github.com")

print(x.text)