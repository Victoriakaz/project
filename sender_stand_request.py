import requests
import json
import configuration 
from data import new_kit_body, kit_body_with_card
user_token = None
new_user_data = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}
def create_new_user(): 
    url = configuration.API_URL + configuration.CREATE_USER_PATH
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(new_user_data))
    return response.json()["authToken"]

def get_new_user_token():
    global user_token  
    if  user_token is None:
        user_token = create_new_user()
    return user_token

def post_new_client_kit(kit_body, auth_token):
    url = API_URL + CREATE_USER_PATH
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.post(url, headers=headers, data=json.dumps(kit_body))
    return response