import requests
import json
from Token import my_token

base_url = "https://x-clients-be.onrender.com"

# получить список компаний
class get_company_list:
    def get_company_list(self, params_to_add=None):
        resp = requests.get(base_url+'/company', params_to_add)
        return resp.json()
    
# создать компанию
class create_company:
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        token_obj = my_token()
        token = token_obj.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(base_url + '/company', json=company, headers=my_headers)
        return resp.json()
# вызов компании по id
class get_id_company:
    def get_id_company():
        resp = get_company_list()
        responce = resp.get_company_list()
        companies_json = json.dumps(responce)
        last_company = json.loads(companies_json)[-1]
        return last_company['id']
