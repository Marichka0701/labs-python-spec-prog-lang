import requests
from typing import List

class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()
        return response.json()
    
    def get_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        response.raise_for_status()
        return response.json()
