from DB_Employee import *
from DB_Company import *
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

# добавление новой компании в общий список и сразу удаление через БД
def test_company_workflowA():
    # получим id последней компании
    comp = Company()  
    before = comp.get_id_company()  

    # создадим компанию
    comp.create_company("Новая компания", "Описание новой компании")

    # получим id последней компании после создания
    after = comp.get_id_company()

    # сравним, разница должна быть равна 1
    assert after - before == 1

    # удалим созданную компанию
    dlt = DB_Company()
    dlt.delete_company(after)

    # получим id последней компании после удаления
    after_delete = comp.get_id_company()

    # сравним, разница должна быть равна 0
    assert after_delete - before == 0

# создание сотрудника с заполненными обязательными полями и удаление через БД
def test_add_employee_full():
    # получим id компании для создания в ней сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # создадим сотрудника
    employee = Employee()
    resp1 = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru",89999999999,"2000-07-15T10:07:34.771", True)

    # запросим id сотрудника
    employee = Employee()
    employee_id = employee.get_id_employee()

    # проверим, что id сотрудника не равен 0
    assert employee_id != 0

    # запросим данные сотрудника по полученному id
    resp2 = employee.get_employee_by_id(employee_id)

    # сравним, что в ответе приходит запрошенный id и проверим статус код, должен быть равен 201
    assert resp2["id"] == employee_id
    assert resp1.status_code == 201

    # удалим сотрудника по id через БД и получим запись о нем
    db_empl = DB_Employee()
    db_empl.delete_employee(employee_id)
    get_empl = db_empl.get_employee_by_id(employee_id)

    # проверим запись удаленного сотрудника в БД. Должно быть None
    assert get_empl == None

# создание сотрудника ЧЕРЕЗ БД с заполненными обязательными полями и удаление 
def test_add_employee_full_db():
    # получим id компании для создания в ней сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # создадим сотрудника
    emp = DB_Employee()
    emp.create_employee("Иван", "Иванов", "89999999999", company_id)

    # получим id сотрудника
    id_emp = emp.get_id_employee_by_company_id(company_id)

    # проверим, что id сотрудника не равен 0
    assert id_emp > 0

    # удалим сотрудника по id через БД и получим запись о нем
    emp.delete_employee(id_emp)
    get_empl = emp.get_employee_by_id(id_emp)

    # проверим запись удаленного сотрудника в БД. Должно быть None
    assert get_empl == None

# статус код 400 при отсутствии данных обязательного поля firstName
def test_add_employee_without_firstName():
    # получим id компании, в которой хотим создать сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # попробуем создать сотрудника
    employee = Employee()
    resp = employee.create_employee("","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)

    # проверим статус код, должен быть равен 400
    assert resp.status_code == 400

# статус код 400 при отсутствии данных обязательного поля lastName
def test_add_employee_without_lastName():
    # получим id компании, в которой хотим создать сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # попробуем создать сотрудника
    employee = Employee()
    resp = employee.create_employee("Иван","","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)

    # проверим статус код, должен быть равен 400
    assert resp.status_code == 400

# статус код 400 при отсутствии данных обязательного поля companyId
def test_add_employee_without_companyId():
    # попробуем создать сотрудника без id компании
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович","","iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)

    # проверим статус код, должен быть равен 400
    assert resp.status_code == 400

# статус код 400 при отсутствии данных обязательного поля email
def test_add_employee_without_email():
    # получим id компании, в которой хотим создать сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # попробуем создать сотрудника
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"","89999999999","2000-07-15T10:07:34.771", True)

    # проверим статус код, должен быть равен 400
    assert resp.status_code == 400

# статус код 500 при отсутствии данных обязательного поля birthdate
def test_add_employee_without_birthdate():
    # получим id компании, в которой хотим создать сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # попробуем создать сотрудника
    employee = Employee()
    resp = employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","","", True)

    # проверим статус код, должен быть равен 500
    assert resp.status_code == 500

# внесем изменения в данные сотрудника 
def test_edit_employee():
    # получим id компании для создания в ней сотрудника
    comp = Company()
    company_id = comp.get_id_company()

    # создадим сотрудника
    employee = Employee()
    employee.create_employee("Иван","Иванов","Иванович",company_id,"iv@mail.ru","89999999999","2000-07-15T10:07:34.771", True)

    # запросим id сотрудника
    employee_id = employee.get_id_employee()

    # внесем изменения в данные запрошенного сотрудника
    lastName = 'lastName'
    email = 'email@edited.ru'
    url = 'url edited'
    phone = 'phone edited'
    isActive = False
    resp = employee.edit_employee(employee_id, lastName, email, url, phone, isActive)

    # сравним, что изменения, которые внесли приходят в ответе соответственно
    assert resp['id'] == employee_id
    assert resp['isActive'] == isActive
    assert resp['email'] == email
    assert resp['url'] == url

    # удалим сотрудника по id через БД и получим запись о нем
    db_empl = DB_Employee()
    db_empl.delete_employee(employee_id)
    get_empl = db_empl.get_employee_by_id(employee_id)

    # проверим запись удаленного сотрудника в БД. Должно быть None
    assert get_empl == None

# внесем изменения в данные сотрудника через БД
def test_edit_employee_db():
    # получим id компании, где создадим сотрудника
    comp = DB_Company()
    company_id = comp.get_company_id()

    # создадим сотрудника
    emp = DB_Employee()
    emp.create_employee("NewName", "NewName", "89999999999", company_id)

    # получим id этого сотрудника
    employee_id = emp.get_id_employee_by_company_id(company_id)

    # внесем изменения в запись нового сотрудника
    first_name = 'edited'
    last_name = 'edited'
    phone = 'edited'
    emp.edit_employee(first_name, last_name, phone, employee_id)

    # получим данные по измененному сотруднику
    new_employee_data = emp.get_employee_by_id(employee_id)

    # сравним, что изменения, которые внесли отображаются в БД соответственно
    assert  new_employee_data["first_name"] == first_name
    assert new_employee_data["last_name"] == last_name
    assert new_employee_data["phone"] == phone

    # удалим сотрудника по id через БД и получим запись о нем
    emp.delete_employee(employee_id)
    get_empl = emp.get_employee_by_id(employee_id)

    # проверим запись удаленного сотрудника в БД. Должно быть None
    assert get_empl == None
    