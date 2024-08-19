from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
db = create_engine(db_connection_string)

class DB_Employee:
    """
    Этот класс описывает работу с Сотрудниками через Базу Данных
    """
    def create_employee(self, first_name: str, last_name: str, phone: int, company_id: int) -> tuple:
        """
        создать сотрудника
        """
        sql = text('insert into employee ("first_name", "last_name", "phone", "company_id") values(:first_name, :last_name, :phone, :id)')
        rows = db.execute(sql, first_name=first_name, last_name=last_name, phone=phone, id = company_id)
        return rows
    def get_id_employee_by_company_id(self, company_id: int) -> int:
        """
        Получить максимальный id сотрудника по id компании
        """
        sql = text('select max(id) from employee where company_id = :id')
        rows = db.execute(sql, id = company_id)
        return rows.scalar()
    def edit_employee(self, first_name: str, last_name: str, phone: int, empl_id: int) -> tuple:
        """
        Изменить сотрудника по его id
        """
        sql = text('update employee set first_name = :first_name,last_name = :last_name,phone = :phone where id =:id')
        rows = db.execute(sql, first_name=first_name, last_name=last_name, phone=phone, id=empl_id)
        return rows
    def delete_employee(self, emp_id: int) -> tuple:
        """
        Удалить сотрудника по его id
        """
        sql = text("delete from employee where id = :id")
        rows = db.execute(sql, id = emp_id)
        return rows
    def get_employee_by_id(self, emp_id: int) -> tuple:
        """
        Получить данные сотрудника по его id
        """
        sql = text("select * from employee where id = :id")
        rows = db.execute(sql, id = emp_id).fetchone()
        return rows
    