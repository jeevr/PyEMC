from _ui_functions.database_data import DataBase

db = DataBase()

# print(db.get_db_path())

# makers = db.get_makers_table_data()
# print(makers)

categories = db.get_categories_table_data()
print(categories, type(categories))
for a,b in categories:
    print(a, b)


# db.insert_new_category('test cat2')

# categories = db.get_categories_table_data()
# print(categories)

# db.insert_new_maker('maker', 'model_no', 'category', 'description', 'remarks', 'maker_file_link', 'symbol_link', 'notes')

# makers = db.get_makers_table_data()
# print(makers)