# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainknKrfu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 601)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.sw_1 = QWidget()
        self.sw_1.setObjectName(u"sw_1")
        self.lbl_welcome = QLabel(self.sw_1)
        self.lbl_welcome.setObjectName(u"lbl_welcome")
        self.lbl_welcome.setGeometry(QRect(140, 90, 651, 291))
        self.lbl_welcome.setWordWrap(True)
        self.btn_1 = QPushButton(self.sw_1)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(360, 360, 211, 71))
        self.btn_settings = QPushButton(self.sw_1)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(810, 530, 75, 31))
        self.stackedWidget.addWidget(self.sw_1)
        self.sw_2 = QWidget()
        self.sw_2.setObjectName(u"sw_2")
        self.horizontalLayout_2 = QHBoxLayout(self.sw_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.body_2 = QFrame(self.sw_2)
        self.body_2.setObjectName(u"body_2")
        self.body_2.setFrameShape(QFrame.StyledPanel)
        self.body_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.body_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_buttons = QFrame(self.body_2)
        self.frm_buttons.setObjectName(u"frm_buttons")
        self.frm_buttons.setFrameShape(QFrame.StyledPanel)
        self.frm_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_refresh = QPushButton(self.frm_buttons)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_refresh)

        self.btn_update = QPushButton(self.frm_buttons)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_update)

        self.btn_add = QPushButton(self.frm_buttons)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.frm_buttons)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.frm_buttons)

        self.frm_table = QFrame(self.body_2)
        self.frm_table.setObjectName(u"frm_table")
        self.frm_table.setFrameShape(QFrame.StyledPanel)
        self.frm_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_table)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tbl_1 = QTableWidget(self.frm_table)
        if (self.tbl_1.columnCount() < 9):
            self.tbl_1.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_1.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tbl_1.setObjectName(u"tbl_1")
        self.tbl_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_1.setSortingEnabled(False)

        self.verticalLayout_2.addWidget(self.tbl_1)


        self.verticalLayout.addWidget(self.frm_table)


        self.horizontalLayout_2.addWidget(self.body_2)

        self.stackedWidget.addWidget(self.sw_2)
        self.sw_3 = QWidget()
        self.sw_3.setObjectName(u"sw_3")
        self.horizontalLayout_4 = QHBoxLayout(self.sw_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.body_3 = QFrame(self.sw_3)
        self.body_3.setObjectName(u"body_3")
        self.body_3.setFrameShape(QFrame.StyledPanel)
        self.body_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.body_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_1 = QLabel(self.frame)
        self.lbl_1.setObjectName(u"lbl_1")

        self.horizontalLayout_6.addWidget(self.lbl_1)

        self.btn_back = QPushButton(self.frame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_6.addWidget(self.btn_back)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.body_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_2 = QLabel(self.frame_2)
        self.lbl_2.setObjectName(u"lbl_2")

        self.horizontalLayout_5.addWidget(self.lbl_2)

        self.txt_db_path = QTextEdit(self.frame_2)
        self.txt_db_path.setObjectName(u"txt_db_path")
        self.txt_db_path.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.txt_db_path)

        self.btn_sel_db_path = QPushButton(self.frame_2)
        self.btn_sel_db_path.setObjectName(u"btn_sel_db_path")
        self.btn_sel_db_path.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.btn_sel_db_path)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.body_3)

        self.stackedWidget.addWidget(self.sw_3)
        self.sw_4 = QWidget()
        self.sw_4.setObjectName(u"sw_4")
        self.horizontalLayout_7 = QHBoxLayout(self.sw_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_3 = QFrame(self.sw_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 110, 131, 16))
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(320, 110, 241, 31))
        self.btn_add_cat = QPushButton(self.frame_3)
        self.btn_add_cat.setObjectName(u"btn_add_cat")
        self.btn_add_cat.setGeometry(QRect(580, 110, 51, 31))
        self.btn_save_cat = QPushButton(self.frame_3)
        self.btn_save_cat.setObjectName(u"btn_save_cat")
        self.btn_save_cat.setGeometry(QRect(780, 510, 75, 31))
        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(320, 160, 241, 291))
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 460, 101, 31))
        self.btn_cancel_cat = QPushButton(self.frame_3)
        self.btn_cancel_cat.setObjectName(u"btn_cancel_cat")
        self.btn_cancel_cat.setGeometry(QRect(30, 510, 75, 31))

        self.horizontalLayout_7.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.sw_4)
        self.sw_5 = QWidget()
        self.sw_5.setObjectName(u"sw_5")
        self.horizontalLayout_8 = QHBoxLayout(self.sw_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_4 = QFrame(self.sw_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_4 = QLabel(self.frame_6)
        self.lbl_4.setObjectName(u"lbl_4")

        self.horizontalLayout_10.addWidget(self.lbl_4)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 100, 101, 16))
        self.txt_model_no = QTextEdit(self.frame_5)
        self.txt_model_no.setObjectName(u"txt_model_no")
        self.txt_model_no.setGeometry(QRect(340, 90, 241, 31))
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 140, 101, 16))
        self.txt_desc = QTextEdit(self.frame_5)
        self.txt_desc.setObjectName(u"txt_desc")
        self.txt_desc.setGeometry(QRect(340, 170, 241, 31))
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 180, 101, 16))
        self.cbo_cat = QComboBox(self.frame_5)
        self.cbo_cat.setObjectName(u"cbo_cat")
        self.cbo_cat.setGeometry(QRect(340, 130, 241, 31))
        self.txt_remarks = QTextEdit(self.frame_5)
        self.txt_remarks.setObjectName(u"txt_remarks")
        self.txt_remarks.setGeometry(QRect(340, 210, 241, 31))
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 220, 101, 16))
        self.txt_maker_link = QTextEdit(self.frame_5)
        self.txt_maker_link.setObjectName(u"txt_maker_link")
        self.txt_maker_link.setGeometry(QRect(340, 250, 241, 31))
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 260, 101, 16))
        self.txt_symbol_link = QTextEdit(self.frame_5)
        self.txt_symbol_link.setObjectName(u"txt_symbol_link")
        self.txt_symbol_link.setGeometry(QRect(340, 290, 241, 31))
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 300, 101, 16))
        self.btn_attach_file = QPushButton(self.frame_5)
        self.btn_attach_file.setObjectName(u"btn_attach_file")
        self.btn_attach_file.setGeometry(QRect(590, 250, 51, 31))
        self.btn_attach_symbol = QPushButton(self.frame_5)
        self.btn_attach_symbol.setObjectName(u"btn_attach_symbol")
        self.btn_attach_symbol.setGeometry(QRect(590, 290, 51, 31))
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 340, 101, 16))
        self.txt_notes = QTextEdit(self.frame_5)
        self.txt_notes.setObjectName(u"txt_notes")
        self.txt_notes.setGeometry(QRect(340, 330, 241, 101))
        self.btn_add_category = QPushButton(self.frame_5)
        self.btn_add_category.setObjectName(u"btn_add_category")
        self.btn_add_category.setGeometry(QRect(590, 130, 51, 31))
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(210, 60, 101, 16))
        self.txt_maker = QTextEdit(self.frame_5)
        self.txt_maker.setObjectName(u"txt_maker")
        self.txt_maker.setGeometry(QRect(340, 50, 241, 31))
        self.btn_cancel_add = QPushButton(self.frame_5)
        self.btn_cancel_add.setObjectName(u"btn_cancel_add")
        self.btn_cancel_add.setGeometry(QRect(20, 440, 75, 31))
        self.btn_save_add = QPushButton(self.frame_5)
        self.btn_save_add.setObjectName(u"btn_save_add")
        self.btn_save_add.setGeometry(QRect(770, 440, 75, 31))
        self.txt_id = QTextEdit(self.frame_5)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(340, 10, 241, 31))
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(210, 20, 101, 16))
        self.btn_save_update = QPushButton(self.frame_5)
        self.btn_save_update.setObjectName(u"btn_save_update")
        self.btn_save_update.setGeometry(QRect(780, 440, 75, 31))

        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_8.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.sw_5)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Welcome to</span></p><p align=\"center\"><span style=\" font-size:48pt;\">EDG Compiled Makers</span></p></body></html>", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Search for Makers", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update Maker", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add Maker", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Maker", None))
        ___qtablewidgetitem = self.tbl_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tbl_1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MAKER", None));
        ___qtablewidgetitem2 = self.tbl_1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None));
        ___qtablewidgetitem3 = self.tbl_1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MODEL NO", None));
        ___qtablewidgetitem4 = self.tbl_1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION", None));
        ___qtablewidgetitem5 = self.tbl_1.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None));
        ___qtablewidgetitem6 = self.tbl_1.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"SYMBOL", None));
        ___qtablewidgetitem7 = self.tbl_1.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"LINK", None));
        ___qtablewidgetitem8 = self.tbl_1.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NOTES", None));
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Database Connection Settings</span></p></body></html>", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.lbl_2.setText(QCoreApplication.translate("MainWindow", u"Database Folder Path", None))
        self.btn_sel_db_path.setText(QCoreApplication.translate("MainWindow", u"change", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW CATEGORY NAME", None))
        self.btn_add_cat.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.btn_save_cat.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Category", None))
        self.btn_cancel_cat.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lbl_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Add New Maker / Update Maker</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MODEL NO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MAKER FILE LINK", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SYMBOL LINK", None))
        self.btn_attach_file.setText(QCoreApplication.translate("MainWindow", u"attach", None))
        self.btn_attach_symbol.setText(QCoreApplication.translate("MainWindow", u"attach", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"NOTES", None))
        self.btn_add_category.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"MAKER", None))
        self.btn_cancel_add.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_save_add.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.txt_id.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Auto generated</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.btn_save_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

