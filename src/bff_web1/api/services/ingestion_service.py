import requests
from models.user import User

MICROSERVICE_URL = "http://user-service/api/users"

def get_users():
    response = requests.get(MICROSERVICE_URL)
    if response.status_code == 200:
        return response.json()
    raise Exception("Error fetching users")

def create_user(user: User):
    response = requests.post(MICROSERVICE_URL, json=user.dict())
    if response.status_code == 201:
        return response.json()
    raise Exception("Error creating user")
