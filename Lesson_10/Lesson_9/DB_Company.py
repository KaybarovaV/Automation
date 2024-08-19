from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
db = create_engine(db_connection_string)

class DB_Company:
    """
    Этот класс описывает работу с Компаниями через Базу Данных
    """
    # 
    def get_company_id(self) -> int:
        """
        Получить максимальный id компании 
        """
        row = db.execute("select max(id) from company").fetchone()
        return row[0]
    def delete_company(self, comp_id: int) -> tuple:
        """
        Удалить компанию по id, введенному в параметре
        """
        sql = text("delete from company where id = :id")
        rows = db.execute(sql, id = comp_id)
        return rows