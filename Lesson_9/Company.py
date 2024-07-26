import requests

base_url = "https://x-clients-be.onrender.com"

class Company:
    # получить токен
    def my_token(self, user='leyla', password='water-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken']
    
    # получить список компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(base_url+'/company', params_to_add)
        return resp.json()
    
    # создать компанию
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        token = self.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(base_url + '/company', json=company, headers=my_headers)
        return resp.json()
    
    # вызов компании по id
    def get_id_company(self):
        resp = self.get_company_list()
        last_company = resp[-1]
        return last_company['id']