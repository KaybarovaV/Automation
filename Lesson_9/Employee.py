import requests
from Company import *

base_url = "https://x-clients-be.onrender.com"

class Employee:
    # получить токен
    def my_token(self, user='leyla', password='water-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken']
    
    # получить список сотрудников по id компании
    def get_employee(self, company_id):
        resp = requests.get(base_url+'/employee', params={'company': company_id})
        return resp.json()
    
    # добавить нового сотрудника для компании 
    def create_employee(self, firstName, lastName, middleName, companyId, email, phone, birthdate, isActive):
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
    
    # получить id сотрудника
    def get_id_employee(self):
        comp = Company()
        id_comp = comp.get_id_company()
        resp = self.get_employee(id_comp)
        return resp[0]['id']
    
    # получить сотрудника по его id
    def get_employee_by_id(self, employee_id):
        id_empl = self.get_id_employee()
        resp = requests.get(base_url+'/employee/'+str(id_empl))
        return resp.json()

    # изменить информацию о сотруднике
    def edit_employee(self, employee_id, lastName, email, url, phone, isActive):
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