# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popupdVgfaK.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_popup(object):
    def setupUi(self, popup):
        if not popup.objectName():
            popup.setObjectName(u"popup")
        popup.resize(330, 146)
        popup.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(popup)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(popup)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_diag_cancel = QPushButton(self.frame_2)
        self.btn_diag_cancel.setObjectName(u"btn_diag_cancel")
        self.btn_diag_cancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_diag_cancel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bnt_diag_delete = QPushButton(self.frame_2)
        self.bnt_diag_delete.setObjectName(u"bnt_diag_delete")
        self.bnt_diag_delete.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.bnt_diag_delete)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.retranslateUi(popup)

        QMetaObject.connectSlotsByName(popup)
    # setupUi

    def retranslateUi(self, popup):
        popup.setWindowTitle(QCoreApplication.translate("popup", u"Form", None))
        self.label.setText(QCoreApplication.translate("popup", u"<html><head/><body><p>Are you sure you want to delete the selected Maker? </p><p>This will delete all the data related to the maker.</p></body></html>", None))
        self.btn_diag_cancel.setText(QCoreApplication.translate("popup", u"Cancel", None))
        self.bnt_diag_delete.setText(QCoreApplication.translate("popup", u"Delete", None))
    # retranslateUi

