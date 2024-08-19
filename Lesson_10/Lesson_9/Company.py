import requests

base_url = "https://x-clients-be.onrender.com"

class Company:
    """
    Этот класс описывает работу с Компаниями. 
    """
    def my_token(self, user='leyla', password='water-fairy') -> str:
        """
        Получить токен с логином leyla и паролем water-fairy
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken']
    def get_company_list(self, params_to_add=None) -> list:
        """
        Получить список компаний
        """
        resp = requests.get(base_url+'/company', params_to_add)
        return resp.json()
    def create_company(self, name:str, description:str) -> str:
        """
        Cоздать компанию авторизованным пользователем
        """
        company = {
            "name": name,
            "description": description
        }
        token = self.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(base_url + '/company', json=company, headers=my_headers)
        return resp.json()
    def get_id_company(self) -> int:
        """
        Получить id компании последней в списке
        """
        resp = self.get_company_list()
        last_company = resp[-1]
        return last_company['id']