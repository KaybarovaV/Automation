from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
db = create_engine(db_connection_string)

class DB_Company:
    # получить список компаний
    def get_company_id(self):
        row = db.execute("select max(id) from company").fetchone()
        return row[0]
    
    # удалить компанию
    def delete_company(self, comp_id):
        sql = text("delete from company where id = :id")
        rows = db.execute(sql, id = comp_id)
        return rows