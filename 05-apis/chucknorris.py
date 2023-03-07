import json

import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)

# print(response.text['value'])

data = json.loads(response.text)

print(data['value'])



