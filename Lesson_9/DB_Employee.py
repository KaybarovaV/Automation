from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
db = create_engine(db_connection_string)

class DB_Employee:
    # создать сотрудника
    def create_employee(self, first_name, last_name, phone, company_id):
        sql = text('insert into employee ("first_name", "last_name", "phone", "company_id") values(:first_name, :last_name, :phone, :id)')
        rows = db.execute(sql, first_name=first_name, last_name=last_name, phone=phone, id = company_id)
        return rows
    
    # получить id сотрудника по id компании
    def get_id_employee_by_company_id(self, company_id):
        sql = text('select max(id) from employee where company_id = :id')
        rows = db.execute(sql, id = company_id)
        return rows.scalar()
    
    # изменить сотрудника по его id
    def edit_employee(self, first_name, last_name, phone, empl_id):
        sql = text('update employee set first_name = :first_name,last_name = :last_name,phone = :phone where id =:id')
        rows = db.execute(sql, first_name=first_name, last_name=last_name, phone=phone, id=empl_id)
        return rows
    
    # удалить сотрудника по его id
    def delete_employee(self, emp_id):
        sql = text("delete from employee where id = :id")
        rows = db.execute(sql, id = emp_id)
        return rows
    
    # получить данные сотрудника по его id
    def get_employee_by_id(self, emp_id):
        sql = text("select * from employee where id = :id")
        rows = db.execute(sql, id = emp_id).fetchone()
        return rows
