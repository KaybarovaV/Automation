import requests
from Token import my_token
from Company import get_id_company

base_url = "https://x-clients-be.onrender.com"

# получить список сотрудников по id компании
class get_employee:
    def get_employee(self, company_id):
        resp = requests.get(base_url+'/employee', params={'company': company_id})
        return resp.json()
# добавить нового сотрудника для компании 
class create_employee:
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
        token_obj = my_token()
        token = token_obj.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(base_url + '/employee', json=employee, headers=my_headers)
        return resp
    
# получить id сотрудника
class get_id_employee:
    def get_id_employee():
        id_comp = get_id_company.get_id_company()
        resp = get_employee().get_employee(id_comp)
        return resp[0]['id']
    
# получить сотрудника по его id
class get_employee_by_id:
    def get_employee_by_id(employee_id):
        id_empl = get_id_employee.get_id_employee()
        resp = requests.get(base_url+'/employee/'+str(id_empl))
        return resp.json()

# изменить информацию о сотруднике
class edit_employee:
    def edit_employee(employee_id, lastName, email, url, phone, isActive):
        new_data_employee = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }
        token_obj = my_token()
        token = token_obj.my_token()
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.patch(base_url + '/employee/' + str(employee_id), headers=my_headers, json=new_data_employee)
        return resp.json()




