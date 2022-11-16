import requests
from requests.auth import HTTPBasicAuth
import json

def get_token():
    url= "http://localhost:8080/auth/realms/demo/protocol/openid-connect/token"
    payload = 'grant_type=client_credentials'
    headers = {
    'Content-Type':'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data = payload, 
            auth=HTTPBasicAuth("demoapp","HhSljqj7AU1uJO0uwG8YB3O7PgGVLG6t"))
    token = json.loads(response.text)
    return token["access_token"]


def get_users(token):
    url = "http://localhost:8080/auth/admin/realms/demo/users"
    payload = {}
    headers = {
    'Authorization': 'Bearer '+token}
    response = requests.request("GET", url, headers=headers, data = payload)
    users = json.loads(response.text)
    return users

print(get_users(get_token()))
