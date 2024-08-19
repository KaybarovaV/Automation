import requests
from Company import *

base_url = "https://x-clients-be.onrender.com"

class Employee:
    """
    Этот класс описывает работу с Сотрудниками
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
    def get_employee(self, company_id: int) -> list:
        """
        получить список сотрудников по id компании
        """
        resp = requests.get(base_url+'/employee', params={'company': company_id})
        return resp.json()
    def create_employee(self, firstName: str, lastName: str, middleName: str, companyId: int, email: str, phone: int, birthdate: str, isActive: bool) -> str:
        """
        Добавить нового сотрудника для компании 
        """
        employee = {
            "id": 0,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": "string",
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
            }
        token = self.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(base_url + '/employee', json=employee, headers=my_headers)
        return resp
    def get_id_employee(self) -> int:
        """
        Получить id сотрудника
        """
        comp = Company()
        id_comp = comp.get_id_company()
        resp = self.get_employee(id_comp)
        return resp[0]['id']
    def get_employee_by_id(self, employee_id: int) -> str:
        """
        Получить сотрудника по его id
        """
        id_empl = self.get_id_employee()
        resp = requests.get(base_url+'/employee/'+str(id_empl))
        return resp.json()
    def edit_employee(self, employee_id: int, lastName: str, email: str, url: str, phone: int, isActive: bool) -> str:
        """
        Изменить информацию о сотруднике
        """
        new_data_employee = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }
        token = self.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.patch(base_url + '/employee/' + str(employee_id), headers=my_headers, json=new_data_employee)
        return resp.json()