
import os
import sys

from _gui.ui_main import *
from _ui_functions.database_data import DataBase
from _ui_functions.main_list import MakerTable



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedWidth(920)
        self.setFixedHeight(600)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_1)
        
        # BUTTON FUNCTIONS
        self.ui.btn_1.clicked.connect(lambda: self.load_makers_table())
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sw_3))
        self.ui.btn_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sw_2))
        self.ui.btn_add.clicked.connect(lambda: self.add_new_maker())
        self.ui.btn_add_category.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sw_4))
        self.ui.btn_save_add.clicked.connect(lambda: self.save_new_maker())
        self.ui.btn_delete.clicked.connect(lambda: self.delete_maker_item())
        self.ui.btn_update.clicked.connect(lambda: self.update_maker())
        self.ui.btn_save_update.clicked.connect(lambda: self.save_maker_update())

        self.ui.btn_refresh.clicked.connect(lambda: self.load_makers_table())

        self.show()
 


    def load_makers_table(self):
        self.ui.tbl_1.clearContents()
        self.ui.tbl_1.setRowCount(0)
        
        
        db = DataBase()
        makers_data = db.get_makers_table_data()
        MakerTable.load_data(self, makers_data)

        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_2)

    def add_new_maker(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_5)

        self.ui.lbl_4.setText('Add New Maker Information')
        self.ui.btn_save_add.setVisible(True)
        self.ui.btn_save_update.setVisible(False)
        
        # LOAD CATEGORIES INTO COMBOBOX
        db = DataBase()
        cat_data = db.get_categories_table_data()
        for key, val in cat_data:
            self.ui.cbo_cat.addItem(val)

    def update_maker(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_5)

        self.ui.lbl_4.setText('Update Maker Information')
        self.ui.btn_save_add.setVisible(False)
        self.ui.btn_save_update.setVisible(True)

        # LOAD CATEGORIES INTO COMBOBOX
        db = DataBase()
        cat_data = db.get_categories_table_data()
        for key, val in cat_data:
            self.ui.cbo_cat.addItem(val)

        # GET CURRENT SELECTED ROW INDEX
        selected_row = self.ui.tbl_1.currentRow()

        row_items = []
        for item in range(9):
            print('index', item)
            try:
                cell_val = self.ui.tbl_1.item(selected_row, item).text()
            except:
                cell_val = ''
            row_items.append(cell_val)
        print('cell values', row_items)

        self.ui.txt_id.setText(row_items[0])
        self.ui.txt_maker.setText(row_items[1])
        self.ui.cbo_cat.setCurrentText(row_items[2])
        self.ui.txt_model_no.setText(row_items[3])
        self.ui.txt_desc.setText(row_items[4])
        self.ui.txt_remarks.setText(row_items[5])
        self.ui.txt_symbol_link.setText(row_items[6])
        self.ui.txt_maker_link.setText(row_items[7])
        self.ui.txt_notes.setText(row_items[8])

    def save_maker_update(self):
        maker_id = int(self.ui.txt_id.toPlainText().upper())
        maker = self.ui.txt_maker.toPlainText().upper()
        model = self.ui.txt_model_no.toPlainText().upper()
        category = self.ui.cbo_cat.currentText().upper()
        description = self.ui.txt_desc.toPlainText().upper()
        remarks = self.ui.txt_remarks.toPlainText().upper()
        file_link = self.ui.txt_maker_link.toPlainText().upper()
        symbol_link = self.ui.txt_symbol_link.toPlainText().upper()
        notes = self.ui.txt_notes.toPlainText()

        db = DataBase()
        db.update_maker_item(maker_id, maker, category, model, description, remarks, symbol_link, file_link, notes)

        self.load_makers_table()

        self.ui.txt_maker.setText('')
        self.ui.txt_model_no.setText('')
        self.ui.cbo_cat.clear()
        self.ui.txt_desc.setText('')
        self.ui.txt_remarks.setText('')
        self.ui.txt_maker_link.setText('')
        self.ui.txt_symbol_link.setText('')
        self.ui.txt_notes.setText('')



    def save_new_maker(self):
        maker = self.ui.txt_maker.toPlainText().upper()
        model = self.ui.txt_model_no.toPlainText().upper()
        category = self.ui.cbo_cat.currentText().upper()
        description = self.ui.txt_desc.toPlainText().upper()
        remarks = self.ui.txt_remarks.toPlainText().upper()
        file_link = self.ui.txt_maker_link.toPlainText().upper()
        symbol_link = self.ui.txt_symbol_link.toPlainText().upper()
        notes = self.ui.txt_notes.toPlainText()

        db = DataBase()
        db.insert_new_maker(maker, category, model, description, remarks, symbol_link, file_link, notes)

        self.load_makers_table()

        self.ui.txt_maker.setText('')
        self.ui.txt_model_no.setText('')
        self.ui.cbo_cat.clear()
        self.ui.txt_desc.setText('')
        self.ui.txt_remarks.setText('')
        self.ui.txt_maker_link.setText('')
        self.ui.txt_symbol_link.setText('')
        self.ui.txt_notes.setText('')


    def delete_maker_item(self):
        # GET CURRENT SELECTED ROW INDEX
        selected_row = self.ui.tbl_1.currentRow()
        
        index_val = self.ui.tbl_1.item(selected_row, 0).text()
        index_val_x = self.ui.tbl_1.item(selected_row, 1).text()
        print(selected_row, index_val, index_val_x)

        # DELETE ITEM FROM DATABASE
        db = DataBase()
        db.delete_maker_item(int(index_val))
        self.load_makers_table()


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon('sharingan.ico'))
    window = MainWindow()
    
    # show GUI window form
    
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    app.exec()

    # pyinstaller.exe --icon=sharingan.ico --onefile --noconsole --name=Py-AutoFab main.py