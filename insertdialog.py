from PyQt6 import QtGui
from PyQt6.QtCore import QRegularExpression, Qt, QDateTime
from PyQt6.QtGui import QValidator, QRegularExpressionValidator
from PyQt6.QtWidgets import QDialog

import ui_itemdialog


class InsertDialog(QDialog, ui_itemdialog.Ui_Dialog):

    def __init__(self, sql):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("手动录入")
        self.lineEdit_id.setReadOnly(False)
        self.toolButton_cancel.clicked.connect(self.close)
        self.sql = sql
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        qreg = QRegularExpression('[0-9]{6,11}')
        validator = QRegularExpressionValidator(qreg)
        self.lineEdit_send_tel.setValidator(validator)
        self.lineEdit_hav_tel.setValidator(validator)
        self.lineEdit_id.setValidator(validator)

        self.dateTimeEdit_submit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_sign.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_arrival.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_receipt.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.state_changed()
        self.comboBox_state.currentIndexChanged.connect(self.state_changed)
        self.toolButton_save.clicked.connect(self.save)
        self.dateTimeEdit_sign.dateTimeChanged.connect(self.time_change)
        self.dateTimeEdit_submit.dateTimeChanged.connect(self.time_change)
        self.dateTimeEdit_arrival.dateTimeChanged.connect(self.time_change)
        self.dateTimeEdit_receipt.dateTimeChanged.connect(self.time_change)

    # "2000-01-01 00:00:00" == (self.dateTimeEdit_receipt.dateTime().toString('yyyy-MM-dd hh:mm:ss'))
    def save(self):
        bill_info = [self.lineEdit_id.text(), self.lineEdit_send_name.text(), self.lineEdit_send_tel.text(),
                     self.lineEdit_send_area.text(),
                     self.lineEdit_send_address.text()
            , self.lineEdit_hav_name.text(), self.lineEdit_hav_tel.text(), self.lineEdit_hav_area.text(),
                     self.lineEdit_hav_address.text(), self.comboBox_goods_type.currentText(),
                     self.doubleSpinBox_weight.value(),
                     self.dateTimeEdit_submit.dateTime().toString('yyyy-MM-dd hh:mm:ss'),
                     self.dateTimeEdit_sign.dateTime().toString('yyyy-MM-dd hh:mm:ss'),
                     self.comboBox_state.currentIndex(),
                     self.dateTimeEdit_arrival.dateTime().toString('yyyy-MM-dd hh:mm:ss'),
                     self.dateTimeEdit_receipt.dateTime().toString('yyyy-MM-dd hh:mm:ss')]
        # bill_info = []
        # for i in temp:
        #     if str(i) == "2000-01-01 00:00:00":
        #         bill_info.append('DEFAULT')
        #     else:
        #         bill_info.append(i)
        if self.comboBox_state.currentIndex() == 0:
            bill_info[-4] = 'DEFAULT'
            bill_info[-1] = 'DEFAULT'
            bill_info[-2] = 'DEFAULT'
        elif self.comboBox_state.currentIndex() == 1:
            bill_info[-2] = 'DEFAULT'
        elif self.comboBox_state.currentIndex() == 2:
            bill_info[-1] = 'DEFAULT'

        self.sql.insert_bill(bill_info)
        self.close()
        # print(bill_info)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        # super().keyPressEvent(a0)
        if a0.key() == 16777220:
            self.toolButton_save.click()

    def state_changed(self):
        if self.comboBox_state.currentIndex() == 0:
            self.dateTimeEdit_submit.setEnabled(True)
            self.dateTimeEdit_submit.setMinimumDateTime(QDateTime.currentDateTime())
            self.dateTimeEdit_sign.setEnabled(False)
            self.dateTimeEdit_arrival.setEnabled(False)
            self.dateTimeEdit_receipt.setEnabled(False)
        elif self.comboBox_state.currentIndex() == 1:
            self.dateTimeEdit_submit.setEnabled(True)
            self.dateTimeEdit_sign.setEnabled(True)
            self.dateTimeEdit_sign.setMinimumDateTime(QDateTime.currentDateTime())
            self.dateTimeEdit_arrival.setEnabled(False)
            self.dateTimeEdit_receipt.setEnabled(False)
        elif self.comboBox_state.currentIndex() == 2:
            self.dateTimeEdit_submit.setEnabled(True)
            self.dateTimeEdit_sign.setEnabled(True)
            self.dateTimeEdit_arrival.setEnabled(True)
            self.dateTimeEdit_arrival.setMinimumDateTime(QDateTime.currentDateTime())
            self.dateTimeEdit_receipt.setEnabled(False)
        elif self.comboBox_state.currentIndex() == 3:
            self.dateTimeEdit_submit.setEnabled(True)
            self.dateTimeEdit_sign.setEnabled(True)
            self.dateTimeEdit_arrival.setEnabled(True)
            self.dateTimeEdit_receipt.setEnabled(True)
            self.dateTimeEdit_receipt.setMinimumDateTime(QDateTime.currentDateTime())

    def time_change(self):
        if self.dateTimeEdit_receipt.isEnabled():
            self.dateTimeEdit_receipt.setMinimumDateTime(self.dateTimeEdit_arrival.dateTime())
        if self.dateTimeEdit_arrival.isEnabled():
            self.dateTimeEdit_arrival.setMinimumDateTime(self.dateTimeEdit_sign.dateTime())
        if self.dateTimeEdit_sign.isEnabled():
            self.dateTimeEdit_sign.setMinimumDateTime(self.dateTimeEdit_submit.dateTime())
