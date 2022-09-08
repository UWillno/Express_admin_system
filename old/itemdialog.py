from datetime import datetime
from operator import eq

from PyQt6.QtCore import QDate, QDateTime, Qt
from PyQt6.QtWidgets import QDialog

from ui_itemdialog import Ui_Dialog


class ItemDialog(QDialog, Ui_Dialog):

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.args = list(args)
        self.lineEdit_id.setText(str(args[0]))
        self.lineEdit_send_name.setText(str(args[1]))
        self.lineEdit_send_tel.setText(str(args[2]))
        self.lineEdit_send_area.setText(str(args[3]))
        self.lineEdit_send_address.setText(str(args[4]))
        self.lineEdit_hav_name.setText(str(args[5]))
        self.lineEdit_hav_tel.setText(str(args[6]))
        self.lineEdit_hav_area.setText(str(args[7]))
        self.lineEdit_hav_address.setText(str(args[8]))
        for i in range(self.comboBox_goods_type.count()):
            if eq(self.comboBox_goods_type.itemText(i), args[9]):
                self.comboBox_goods_type.setItemText(i)
                break
        # print(type(args[10]))
        # print(args[10])
        # print(args[11].year)
        # print(args[11].month)
        if isinstance(args[11], datetime):
            dt = args[11]
            self.dateTimeEdit_submit.setDateTime(QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
        if isinstance(args[12], datetime):
            dt = args[12]
            self.dateTimeEdit_sign.setMinimumDateTime(self.dateTimeEdit_submit.dateTime())
            self.dateTimeEdit_sign.setDateTime(QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
        # print(type(args[10]))
        self.doubleSpinBox_weight.setSingleStep(0.5)
        self.doubleSpinBox_weight.setValue(args[10])

        self.toolButton_cancel.clicked.connect(self.cancel)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # print(args[-1])
        # print(type(args[-1]))
        if args[-1] == 1:
            self.comboBox_state.setCurrentIndex(2)
            if args[-2] == 1:
                self.comboBox_state.setCurrentIndex(1)

    def update(self):
        # self.args=list(self.args)
        if self.comboBox_state.currentIndex() == 0:
            # 待录入状态
            self.args[12] = 'DEFAULT'
            self.args[-1] = 0
            self.args[-2] = 0
            # pass
        elif self.comboBox_state.currentIndex() == 1:
            self.args[-1] = 0
            self.args[-2] = 1
        else:
            self.args[-1] = 1
            self.args[-2] = 0
        self.args[1] = self.lineEdit_send_name.text()
        self.args[2] = self.lineEdit_send_tel.text()
        self.args[3] = self.lineEdit_send_area.text()
        self.args[4] = self.lineEdit_send_address.text()
        self.args[5] = self.lineEdit_hav_name.text()
        self.args[6] = self.lineEdit_hav_tel.text()
        self.args[7] = self.lineEdit_hav_area.text()
        self.args[8] = self.lineEdit_hav_address.text()
        self.args[9] = self.comboBox_goods_type.currentText()
        self.args[10] = self.doubleSpinBox_weight.text()

        # pass

    def cancel(self):
        self.close()
