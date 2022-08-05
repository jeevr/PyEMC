from email.mime import image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from _ui_functions.database_data import DataBase

class MainList:
    def __init__(self) -> None:
        pass

class MakerTable:
    def __init__(self):
        pass
    
    def setup_maker_table(self):
        self.ui.tbl_1.verticalHeader().setVisible(False) # HIDE TABLE INDEX
        self.ui.tbl_1.horizontalHeader().setFixedHeight(30) # SET ROW FIX HEIGHT

        # SET COLUMN WIDTH
        self.ui.tbl_1.setColumnWidth(0, 0) # ID
        self.ui.tbl_1.setColumnWidth(1, 80) # MAKER
        self.ui.tbl_1.setColumnWidth(2, 130) # CATERGORY
        self.ui.tbl_1.setColumnWidth(3, 130) # MODEL NO
        self.ui.tbl_1.setColumnWidth(4, 100) # DESCRIPTION
        self.ui.tbl_1.setColumnWidth(5, 80) # REMARKS
        self.ui.tbl_1.setColumnWidth(6, 150) # SYMBOL
        self.ui.tbl_1.setColumnWidth(7, 0) # FILE LINK
        self.ui.tbl_1.setColumnWidth(8, 150) # NOTES


    def load_data(self, db_raw_data):
        MakerTable.setup_maker_table(self)

        print(db_raw_data)
        for row_number, row_data in enumerate(db_raw_data):
            print(row_number, row_data)
            self.ui.tbl_1.insertRow(row_number)
            self.ui.tbl_1.setRowHeight(row_number, 80)

            for column_number, column_data in enumerate(row_data):
                print(column_number, column_data)
                item = str(column_data)
                # if item.isnumeric():
                if column_number == 6:
                    print('inside symbol', column_number)
                   
                    item = get_image_label(column_data)
                    self.ui.tbl_1.setCellWidget(row_number, column_number, item)
                else:
                    self.ui.tbl_1.setItem(row_number, column_number, QTableWidgetItem(item))

    

def get_image_label(image_path):
    db = DataBase()
    root_path = db.get_db_root_path()
    full_path = f'{root_path}\{image_path}'
    print(f'full path: {root_path} + {image_path}')
    print(full_path)
    pixmap = QPixmap(full_path)
    pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    image_label = QLabel()
    image_label.setText('')
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)
    # image_label.setScaledContents(True)
    return image_label