import requests

base_url = "https://x-clients-be.onrender.com"

# авторизоваться и получить токен 
class my_token:
    def my_token(self, user='leyla', password='water-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken']