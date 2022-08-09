from dataclasses import replace
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import insert, Table, MetaData, select, delete, and_, or_

# ref link: https://stackoverflow.com/questions/21206869/insert-and-update-with-core-sqlalchemy
# ref link: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_multiple_tables.htm


class DataBase:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.db_root_path = self.get_db_root_path()

    def get_db_root_path(self):
        f = open('_settings\database_path.txt', 'r')
        f = f.readline().strip()
        return f

    def get_db_path(self): # WILL GET THE DATABASE FOLDER LOCATION FROM THE SPECIFIED TEXT FILE
        try:
            f = self.get_db_root_path()
            path = f'{f}\database\makers.accdb'
            print(path)
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
    
    def get_data_for_filters(self, filter_1):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')
        if filter_1 == 'MAKER':
            qry = select(mytable.c.maker) ##==> RETURN CERTAIN COLUMNS
        elif filter_1 == 'CATEGORY':
            qry = select(mytable.c.category) ##==> RETURN CERTAIN COLUMNS
        elif filter_1 == 'MODEL NO':
            qry = select(mytable.c.model_no) ##==> RETURN CERTAIN COLUMNS
        else:
            return ''
        print(qry)
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

            new_id = result.inserted_primary_key[0]
            
            new_symbol = symbol_link.split('/')[-1]
            # new_symbol_link = os.path.join('FILES', category, str(new_id), new_symbol_link)

            new_maker_file = maker_file_link.split('/')[-1]
            # new_maker_file_link = os.path.join('FILES', category, str(new_id), new_maker_file_link)

            stmt_2 = mytable.update().where(mytable.c.id == new_id).values( symbol=new_symbol,
                                                                            link=new_maker_file)
            result_2 = conn.execute(stmt_2)

            return new_id


    def update_maker_item(self, maker_id, maker, category, model_no, description, remarks, symbol_link, maker_file_link, notes):
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')

        qry = mytable.select().where(mytable.c.id==maker_id) ##==> RETURN CERTAIN COLUMNS
        print(qry)
        with engine.connect() as conn:
            result = conn.execute(qry)
            data = result.fetchall()
            print(data)
            old_symbol_link = data[0][6]
            old_file_link = data[0][7]

            symbol_link = symbol_link.replace('/', '\\')
            maker_file_link = maker_file_link.replace('/', '\\')

            if old_symbol_link in symbol_link:
                symbol_link = old_symbol_link
                print('THE SAME SYMBOL')
            else:
                symbol_link = symbol_link.split('/')[-1]
                symbol_link = os.path.join('FILES', category, str(maker_id), symbol_link)

            if old_file_link in maker_file_link:
                maker_file_link = old_file_link
                print('THE SAME FILE')
            else:
                maker_file_link = maker_file_link.split('/')[-1]
                maker_file_link = os.path.join('FILES', category, str(maker_id), maker_file_link)

            print('$$$$$$$$$$$$$ - OLD', old_symbol_link, old_file_link)
            print('$$$$$$$$$$$$$ - NEW', symbol_link, maker_file_link)


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
        print('maker_id', maker_id)
        engine = self.connect_to_db()
        mytable = self.instantiate_db_tables(engine, 'tbl_makers')

        # qry = mytable.select() #==> LOAD ALL DATA
        # qry = mytable.select().where(mytable.c.cfTeam == 'MED') ##==> WITH SINGLE CONDITION
        # qry = select([mytable.c.cfTeam, mytable.c.cfdwgCode]).where(mytable.c.cfTeam == 'MED') ##==> RETURN CERTAIN COLUMNS
        # my_join = mytable_1.join(mytable_2, mytable_1.c.stdcons_id == mytable_2.c.stdcons_id)
        # qry = select([mytable_1, mytable_2]).select_from(my_join)

        qry = mytable.select().where(mytable.c.id==maker_id) ##==> RETURN CERTAIN COLUMNS
        print(qry)
        with engine.connect() as conn:
            result = conn.execute(qry)
            data = result.fetchall()
        return data