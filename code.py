import requests
from requests.auth import HTTPBasicAuth
url = "http://localhost:8080/auth/realms/demo/protocol/openid-connect/token"

payload = 'grant_type=client_credentials'
headers = {
        'Content-Type':'application/x-www-form-urlencoded'
        }

response = requests.request("POST", url, headers=headers, data = payload, auth=HTTPBasicAuth("demoapp","HhSljqj7AU1uJO0uwG8YB3O7PgGVLG6t"))

print(response.text)

