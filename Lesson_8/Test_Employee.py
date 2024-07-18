from Token import my_token
from Company import get_company_list
from Company import create_company
from Company import get_id_company
from Employee import get_employee_by_id
from Employee import create_employee
from Employee import get_id_employee
from Employee import edit_employee

# токен не равен 0
def test_token():
    token = my_token()
    new_token = token.my_token()
    assert len(new_token) > 0       
# список компаний не пуст
def test_get_companies():
    comp = get_company_list()
    body = comp.get_company_list()
    assert len(body) > 0 
# добавление новой компании в общий список
def test_company_workflow():
    before = get_id_company.get_id_company()
    create_company.create_company("Новая компания", "Описание новой компании")
    after = get_id_company.get_id_company()
    assert after - before == 1
# создание сотрудника с заполненными обязательными полями
def test_add_employee_full():
    company_id = get_id_company.get_id_company()
    employee = create_employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 201
# статус код 400 при отсутствии данных обязательного поля firstName
def test_add_employee_without_firstName():
    company_id = get_id_company.get_id_company()
    employee = create_employee()
    resp = employee.create_employee("","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля lastName
def test_add_employee_without_lastName():
    company_id = get_id_company.get_id_company()
    employee = create_employee()
    resp = employee.create_employee("Иван","","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля companyId
def test_add_employee_without_companyId():
    employee = create_employee()
    resp = employee.create_employee("Иван","Иванов","Иванович","","iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 400 при отсутствии данных обязательного поля email
def test_add_employee_without_email():
    company_id = get_id_company.get_id_company()
    employee = create_employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"","89999999999","2000-07-15T10:07:34.771", True)
    assert resp.status_code == 400
# статус код 500 при отсутствии данных обязательного поля birthdate
def test_add_employee_without_birthdate():
    company_id = get_id_company.get_id_company()
    employee = create_employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","","", True)
    assert resp.status_code == 500
# id сотрудника не равен 0
def test_id_employee():
    resp = get_id_employee.get_id_employee()
    assert resp > 0
# вызывается верный сотрудник по id
def test_get_employee_by_id():
    employee_id = get_id_employee.get_id_employee()
    resp = get_employee_by_id.get_employee_by_id(employee_id)
    assert resp["id"] == employee_id
# все изменения в данных сотрудника сответствуют внесенным изменениям
def test_edit_employee():
    employee_id = get_id_employee.get_id_employee()
    lastName = 'lastName'
    email = 'email@edited.ru'
    url = 'url edited'
    phone = 'phone edited'
    isActive = False
    resp = edit_employee.edit_employee(employee_id, lastName, email, url, phone, isActive)
    assert resp['id'] == employee_id
    assert resp['isActive'] == isActive
    assert resp['email'] == email
    assert resp['url'] == url