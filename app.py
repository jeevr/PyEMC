
from enum import unique
import os
import sys

from _gui.ui_main import *
from _gui.ui_popup import *
from _ui_functions.database_data import DataBase
from _ui_functions.main_list import MakerTable
from _ui_functions.add_new_maker import AddNewMaker

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.del_diag = ConfirmDeleteDialog(parent=self)
        


        self.setFixedWidth(920)
        self.setFixedHeight(600)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_1)
        
        # BUTTON FUNCTIONS
        self.ui.btn_1.clicked.connect(lambda: self.load_makers_table())
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sw_3))
        self.ui.btn_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sw_1))
        self.ui.btn_add.clicked.connect(lambda: self.add_new_maker())
        self.ui.btn_add_category.clicked.connect(lambda: self.add_new_category())
        self.ui.btn_save_add.clicked.connect(lambda: self.save_new_maker())
        self.ui.btn_delete.clicked.connect(lambda: self.delete_maker_confirmation())
        self.del_diag.btn_emit.connect(lambda: self.delete_maker_item())
        self.ui.btn_update.clicked.connect(lambda: self.update_maker())
        self.ui.btn_save_update.clicked.connect(lambda: self.save_maker_update())
        self.ui.btn_cancel_add.clicked.connect(lambda: self.cancel_new_maker_input())
        self.ui.btn_cancel_cat.clicked.connect(lambda: self.cancel_new_category_input())
        self.ui.btn_add_cat.clicked.connect(lambda: self.add_category_to_list())
        self.ui.btn_remove_cat.clicked.connect(lambda: self.delete_category_to_list())
        self.ui.btn_attach_file.clicked.connect(lambda: self.select_file('FILE'))
        self.ui.btn_attach_symbol.clicked.connect(lambda: self.select_file('SYMBOL'))
        self.ui.btn_sel_db_path.clicked.connect(lambda: self.connect_to_backend_database())
        self.ui.cbo_filter_1.currentTextChanged.connect(lambda: self.load_filter_data_2())

        self.ui.btn_apply_filter.clicked.connect(lambda: self.apply_filter())
        self.ui.btn_clear_filter.clicked.connect(lambda: self.clear_filter())
        

        self.ui.btn_refresh.clicked.connect(lambda: self.load_makers_table())

        self.show()
 


    def load_makers_table(self):
        self.ui.tbl_1.clearContents()
        self.ui.tbl_1.setRowCount(0)
        
    
        db = DataBase()
        makers_data = db.get_makers_table_data()
        MakerTable.load_data(self, makers_data)

        self.load_filter_data_1()
        self.ui.cbo_filter_1.setCurrentText('')

        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_2)

    def load_filter_data_1(self):
        self.ui.cbo_filter_1.clear()
        filters_1 = ['', 'MAKER', 'CATEGORY', 'MODEL NO']
        self.ui.cbo_filter_1.addItems(filters_1)
        self.ui.cbo_filter_1.setCurrentText('')
    
    def load_filter_data_2(self):
        filter_data_1 = self.ui.cbo_filter_1.currentText()
        self.ui.cbo_filter_2.clear()
        db = DataBase()
        ret_val = db.get_data_for_filters(filter_data_1)
        print(ret_val)
        # CREATE A LIST FROM THE VALUE
        vals = []
        for val in ret_val:
            vals.append(val[0])
        
        # REMOVE DUPLOCATES FROM LIST USING SET
        unique_vals = [*set(vals)]
        print(unique_vals)
        
        self.ui.cbo_filter_2.addItems(unique_vals)

        self.ui.cbo_filter_2.setCurrentText('')

    def add_new_maker(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_5)

        self.ui.lbl_4.setText('<html><head/><body><p><span style=" font-size:16pt;">Add New Maker</span></p></body></html>')
        self.ui.btn_save_add.setVisible(True)
        self.ui.btn_save_update.setVisible(False)
        
        # LOAD CATEGORIES INTO COMBOBOX
        db = DataBase()
        cat_data = db.get_categories_table_data()
        for key, val in cat_data:
            self.ui.cbo_cat.addItem(val)

    def add_new_category(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_4)

        db = DataBase()
        cat_data = db.get_categories_table_data()
        for key, val in cat_data:
            self.ui.lst_cat.addItem(val)

    def add_category_to_list(self):
        new_item = self.ui.txt_new_cat_entry.toPlainText().upper()
        self.ui.lst_cat.addItem(new_item)
    
    def delete_category_to_list(self):
        listItems = self.ui.lst_cat.selectedItems()
        if not listItems:
            pass
        for item in listItems:
            self.ui.lst_cat.takeItem(self.ui.lst_cat.row(item))

    def cancel_new_maker_input(self):
        self.load_makers_table()
        self.reset_category_labels()

        self.ui.cbo_filter_1.setCurrentText('')
    
    def cancel_new_category_input(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_5)

        self.ui.txt_new_cat_entry.setText('')
        self.ui.lst_cat.clear()

        self.load_filter_data_1()

    def update_maker(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.sw_5)

        self.ui.lbl_4.setText('<html><head/><body><p><span style=" font-size:16pt;">Update Maker Information</span></p></body></html>')
        self.ui.btn_save_add.setVisible(False)
        self.ui.btn_save_update.setVisible(True)

        # GET CURRENT SELECTED ROW INDEX
        selected_row = self.ui.tbl_1.currentRow()
        index_val = int(self.ui.tbl_1.item(selected_row, 0).text())
        print('selected_row', selected_row)
        print('index val', index_val)
        

        # LOAD CATEGORIES INTO COMBOBOX
        db = DataBase()
        root_path = db.get_db_root_path()
        cat_data = db.get_categories_table_data()
        for key, val in cat_data:
            self.ui.cbo_cat.addItem(val)

        # FETCH DATA FROM DATABASE ACCORDINF TO THE INDEX SELECTED
        row_data = db.retrieve_row_data(index_val)
        print('row_data', row_data)

        row_items = row_data[0]

        self.ui.txt_id.setText(str(row_items[0]))
        self.ui.txt_maker.setText(row_items[1])
        self.ui.cbo_cat.setCurrentText(row_items[2])
        self.ui.txt_model_no.setText(row_items[3])
        self.ui.txt_desc.setText(row_items[4])
        self.ui.txt_remarks.setText(row_items[5])
        self.ui.txt_symbol_link.setText(f'{root_path}\{row_items[6]}')
        self.ui.txt_maker_link.setText(f'{root_path}\{row_items[7]}')
        self.ui.txt_notes.setText(row_items[8])

    def reset_category_labels(self):
        self.ui.txt_id.setText('Auto Generated')
        self.ui.txt_maker.setText('')
        self.ui.txt_model_no.setText('')
        self.ui.cbo_cat.clear()
        self.ui.txt_desc.setText('')
        self.ui.txt_remarks.setText('')
        self.ui.txt_maker_link.setText('')
        self.ui.txt_symbol_link.setText('')
        self.ui.txt_notes.setText('')

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
        
        self.reset_category_labels()

        self.load_filter_data_1()

    def save_new_maker(self):
        maker = self.ui.txt_maker.toPlainText().upper()
        model = self.ui.txt_model_no.toPlainText().upper()
        category = self.ui.cbo_cat.currentText().upper()
        description = self.ui.txt_desc.toPlainText().upper()
        remarks = self.ui.txt_remarks.toPlainText().upper()
        file_link = self.ui.txt_maker_link.toPlainText().upper()
        symbol_link = self.ui.txt_symbol_link.toPlainText().upper()
        notes = self.ui.txt_notes.toPlainText()

        # ADD DATA TO DATABASE
        db = DataBase()
        new_maker_id = db.insert_new_maker(maker, category, model, description, remarks, symbol_link, file_link, notes)

        # CREATE DIRECTORY
        add = AddNewMaker()
        add.create_dir(category, new_maker_id)

        # SAVE FILES
        add.copy_files(symbol_link, file_link)

        self.load_makers_table()

        self.reset_category_labels()

        self.load_filter_data_1()

    def delete_maker_confirmation(self):
        self.del_diag.show()

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

    def select_file(self, for_type):
        fdialog = QFileDialog()
        sel_file = fdialog.getOpenFileName(self, 'Select a file')[0]
        print(sel_file)
        if for_type == 'FILE':
            self.ui.txt_maker_link.setText(sel_file)
        if for_type == 'SYMBOL':
            self.ui.txt_symbol_link.setText(sel_file)
            # preview symbol
            x_maker = AddNewMaker()
            x_maker.preview_symbol(sel_file, self.ui.lbl_symbol_img)

        return sel_file

    def connect_to_backend_database(self):
        db_root_path = self.ui.txt_db_path.toPlainText()
        print(db_root_path)

        # CONFIRM IF THE DATABASE IS FOUND
        db_full_path = f'{db_root_path}\database\makers.accdb'
        files_path = f'{db_root_path}\\files\\'

        is_db_exist = os.path.exists(db_full_path)
        is_file_path_exist = os.path.isdir(files_path)
        
        if is_db_exist and is_file_path_exist:

            # WRITE TO THE TEXT FILE
            f = open('_settings\database_path.txt', 'w')
            f.write(db_root_path)
            f.close()

            self.ui.lbl_result.setText('Connected to Database Successfully!')
        else:
            self.ui.lbl_result.setText('Failed connecting to Database. Check the given link.')
         
    def apply_filter(self):
        # GET FILTERS
        filter_1 = self.ui.cbo_filter_1.currentText()
        filter_2 = self.ui.cbo_filter_2.currentText()
        print(filter_1, filter_2)

        # FILTER ITEMS FROM TABLE WIDGET
        # MAKER = 1, CATEGORY = 2, MODEL NO = 3
        row_cnt = self.ui.tbl_1.rowCount()
        col_cnt = self.ui.tbl_1.columnCount()

        for row in range(row_cnt):
            if filter_1 == 'MAKER':
                    cell_item = self.ui.tbl_1.item(row, 1).text()
            elif filter_1 == 'CATEGORY':
                    cell_item = self.ui.tbl_1.item(row, 2).text()
            elif filter_1 == 'MODEL NO':
                    cell_item = self.ui.tbl_1.item(row, 3).text()
            else:
                cell_item = ''

            if cell_item == filter_2:
                self.ui.tbl_1.setRowHidden(row, False)
            else:
                self.ui.tbl_1.setRowHidden(row, True)


    def clear_filter(self):
        self.ui.cbo_filter_1.setCurrentText('')
        self.ui.cbo_filter_2.setCurrentText('')

        row_cnt = self.ui.tbl_1.rowCount()

        for row in range(row_cnt):
            self.ui.tbl_1.setRowHidden(row, False)


class ConfirmDeleteDialog(QWidget):

    btn_emit = Signal(str)

    def __init__(self, parent=None):
        self.parent = parent
        QWidget.__init__(self)
        self.ui = Ui_popup()
        self.ui.setupUi(self)

        # self.setWindowTitle("MY DIALOG")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.button_setup()
        
    def button_setup(self):
        self.ui.btn_diag_cancel.clicked.connect(lambda: self.close())
        self.ui.bnt_diag_delete.clicked.connect(lambda: self.deleted_confirmed())
    
    def deleted_confirmed(self):
        emit_val = 'DELETE CONFIRMED'
        self.btn_emit.emit(emit_val)
        self.close()
        print(emit_val)
    
    def showEvent(self, event):
        if not event.spontaneous():
            geo = self.geometry()
            geo.moveCenter(self.parent.geometry().center())
            QTimer.singleShot(0, lambda: self.setGeometry(geo))


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon('sharingan.ico'))
    window = MainWindow()
    
    # show GUI window form
    
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    app.exec()

    # pyinstaller.exe --icon=sharingan.ico --onefile --noconsole --name=Py-AutoFab main.py