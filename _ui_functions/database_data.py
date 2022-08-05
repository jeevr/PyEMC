
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import insert, Table, MetaData, select, delete, and_, or_

# ref link: https://stackoverflow.com/questions/21206869/insert-and-update-with-core-sqlalchemy
# ref link: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_multiple_tables.htm


class DataBase:
    def __init__(self):
        self.db_path = self.get_db_path()

    def get_db_root_path(self):
        f = open('_settings\database_path.txt', 'r')
        f = f.readline().strip()
        return f

    def get_db_path(self): # WILL GET THE DATABASE FOLDER LOCATION FROM THE SPECIFIED TEXT FILE
        try:
            f = self.get_db_root_path()
            path = f'{f}\database\makers.accdb'
            return path
        except:
            return 'ERROR IN PARSING DATABASE PATH'

    def connect_to_db(self):
        access_driver = 'Microsoft Access Driver (*.mdb, *.accdb)'
    
        # CREATE CONNECTION STRING
        conn_str = (r'DRIVER={'+access_driver+'};'
                    r'DBQ='+self.db_path+';')
        connection_url = URL.create("access+pyodbc", query={"odbc_connect": conn_str})
        engine = create_engine(connection_url)
        return engine

    def instantiate_db_tables(self, engine, table_name): # INSTANTIATE THE REFERENCE TABLE
        # link: https://docs.sqlalchemy.org/en/14/core/reflection.html
        metadata_obj = MetaData()
        metadata_obj.reflect(bind=engine)
        mytable = metadata_obj.tables[table_name]
        # addresses_table = metadata_obj.tables['addresses']
        return mytable

    def get_makers_table_data(self):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')
        qry = mytable.select()
        with engine.connect() as conn:
            result = conn.execute(qry)
            data = result.fetchall()
        return data

    def get_categories_table_data(self):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_categories')
        qry = mytable.select()
        with engine.connect() as conn:
            result = conn.execute(qry)
            data = result.fetchall()
        return data
    
    def insert_new_category(self, category_name):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_categories')
        stmt = mytable.insert().values(category=category_name)
        with engine.connect() as conn:
            result = conn.execute(stmt)

    def insert_new_maker(self, maker, category, model_no, description, remarks, symbol_link, maker_file_link, notes):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')
        stmt = mytable.insert().values( maker=maker,
                                        category=category,
                                        model_no=model_no,
                                        description=description,
                                        remarks=remarks,
                                        symbol=symbol_link,
                                        link=maker_file_link,
                                        notes=notes)
        with engine.connect() as conn:
            result = conn.execute(stmt)

    def update_maker_item(self, maker_id, maker, category, model_no, description, remarks, symbol_link, maker_file_link, notes):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')
        stmt = mytable.update().where(mytable.c.id == maker_id).values( maker=maker,
                                                                        category=category,
                                                                        model_no=model_no,
                                                                        description=description,
                                                                        remarks=remarks,
                                                                        symbol=symbol_link,
                                                                        link=maker_file_link,
                                                                        notes=notes)
        with engine.connect() as conn:
            result = conn.execute(stmt)

    def delete_maker_item(self, maker_id):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')
        stmt = mytable.delete().where(mytable.c.id==maker_id)

        with engine.connect() as conn:
            result = conn.execute(stmt)

    def retrieve_row_data(self, maker_id):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')

        # qry = mytable.select() #==> LOAD ALL DATA
        # qry = mytable.select().where(mytable.c.cfTeam == 'MED') ##==> WITH SINGLE CONDITION
        # qry = select([mytable.c.cfTeam, mytable.c.cfdwgCode]).where(mytable.c.cfTeam == 'MED') ##==> RETURN CERTAIN COLUMNS
        # my_join = mytable_1.join(mytable_2, mytable_1.c.stdcons_id == mytable_2.c.stdcons_id)
        # qry = select([mytable_1, mytable_2]).select_from(my_join)

        qry = select([mytable.c.id]).where(and_(mytable.c.stdcons_id == std_cons_id, mytable.c.shipno == ship_no, mytable.c.inputted_by == pc_name, mytable.c.consul_no == consulno)) ##==> RETURN CERTAIN COLUMNS

        with engine.connect() as conn:
            result = conn.execute(qry)

            data = result.fetchall()