import shutil
import os
import sys
from _ui_functions.database_data import DataBase

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class AddNewMaker:
    def __init__(self) -> None:
        self.root_path = ''
        self.new_dir_path = ''

    # def create_dir(self, category, maker_id):
    #     # THIS WILL CREATE DIRECTORY BASED ON THE CATEGORY AND THE ID IN THE DATABASE
    #     db = DataBase()
    #     self.root_path = db.get_db_root_path()

    #     # COMPLETE THE PATH
    #     self.new_dir_path = os.path.join(self.root_path, 'FILES', category, str(maker_id))

    #     # CREATE THE DIRECTORY
    #     try:
    #         os.makedirs(self.new_dir_path)
    #         print(self.new_dir_path)
    #     except:
    #         return 'FAILED CREATING  DIRECTORY'
    
    def create_dir(self, category, maker_id):
        # THIS WILL CREATE DIRECTORY BASED ON THE CATEGORY AND THE ID IN THE DATABASE
        db = DataBase()
        self.root_path = db.get_db_root_path()

        # COMPLETE THE PATH
        self.new_dir_path = os.path.join(self.root_path, 'FILES', f'{maker_id}-{category}')

        # CREATE THE DIRECTORY
        try:
            os.makedirs(self.new_dir_path)
            print(self.new_dir_path)
        except:
            return 'FAILED CREATING  DIRECTORY'

    def copy_files(self, symbol_link, file_link):
        try:
            symbol_dest = os.path.join(self.new_dir_path, symbol_link.split('/')[-1])
            shutil.copy(symbol_link, symbol_dest)
        except:
            return 'ERROR COPYING FILE'

        try:
            file_dest = os.path.join(self.new_dir_path, file_link.split('/')[-1])
            shutil.copy(file_link, file_dest)
        except:
            return 'ERROR COPYING FILE'

    def preview_symbol(self, img_path, _label):
        try:
            print(img_path)
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaled(200, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            _label.setText('')
            _label.setPixmap(pixmap)
            _label.setAlignment(Qt.AlignCenter)
        except:
            pass