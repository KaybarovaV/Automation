from Company import *
from Employee import *

# токен не равен 0
def test_token():
    token = Employee()
    new_token = token.my_token()
    assert len(new_token) > 0       
# список компаний не пуст
def test_get_companies():
    comp = Company()
    body = comp.get_company_list()
    assert len(body) > 0 
# добавление новой компании в общий список
def test_company_workflow():
    comp = Company()  
    before = comp.get_id_company()  
    comp.create_company("Новая компания", "Описание новой компании")
    after = comp.get_id_company()
    assert after - before == 1
# создание сотрудника с заполненными обязательными полями
def test_add_employee_full():
    comp = Company()
    company_id = comp.get_id_company()
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 201
# статус код 400 при отсутствии данных обязательного поля firstName
def test_add_employee_without_firstName():
    comp = Company()
    company_id = comp.get_id_company()
    employee = Employee()
    resp = employee.create_employee("","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля lastName
def test_add_employee_without_lastName():
    comp = Company()
    company_id = comp.get_id_company()
    employee = Employee()
    resp = employee.create_employee("Иван","","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля companyId
def test_add_employee_without_companyId():
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович","","iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля email
def test_add_employee_without_email():
    comp = Company()
    company_id = comp.get_id_company()
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 500 при отсутствии данных обязательного поля birthdate
def test_add_employee_without_birthdate():
    comp = Company()
    company_id = comp.get_id_company()
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","","", True)
    assert resp.status_code == 500
# id сотрудника не равен 0
def test_id_employee():
    employee = Employee()
    resp = employee.get_id_employee()
    assert resp > 0
# вызывается верный сотрудник по id
def test_get_employee_by_id():
    employee = Employee()
    employee_id = employee.get_id_employee()
    resp = employee.get_employee_by_id(employee_id)
    assert resp["id"] == employee_id
# все изменения в данных сотрудника сответствуют внесенным изменениям
def test_edit_employee():
    employee = Employee()
    employee_id = employee.get_id_employee()
    lastName = 'lastName'
    email = 'email@edited.ru'
    url = 'url edited'
    phone = 'phone edited'
    isActive = False
    resp = employee.edit_employee(employee_id, lastName, email, url, phone, isActive)
    assert resp['id'] == employee_id
    assert resp['isActive'] == isActive
    assert resp['email'] == email
    assert resp['url'] == url