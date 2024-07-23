from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

""" def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = reflection.Inspector.from_engine(db)
    names = inspector.get_table_names()
    assert names[0] == 'app_users' """

 """ def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[-1]
    assert row1[0] == 16127
    assert row1["name"] == "TESTSUPER" """

""" def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement,company_id = 16127).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "TESTSUPER" """

""" def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and id>=:id")

    my_params = {
        'id': 16000,
        'is_active': True
    }
    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 60
    assert rows[0]["name"] == "SkyPro" """
 """
def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company ("name") values (:new_name)")
    rows = db.execute(sql, new_name = 'School')
 """



