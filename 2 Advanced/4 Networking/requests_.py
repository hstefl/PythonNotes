# pip install requests

import requests

response = requests.get('http://localhost:3000')
print(f"Response code: {response.status_code}")
print(f"Response header: {response.headers}", )
print(f"Response header (Content-type): {response.headers['Content-type']}")
print(f"Response body: {response.text}")