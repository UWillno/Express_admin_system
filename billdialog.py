from PyQt6 import QtGui
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QDialog

import ui_itemdialog


class BillItemDialog(QDialog, ui_itemdialog.Ui_Dialog):

    def __init__(self, sql, *args):
        super().__init__()
        self.sql = sql
        self.args = args
        self.setupUi(self)
        self.show()
        # print(type(args[11]))
        self.toolButton_cancel.clicked.connect(self.close)
        qreg = QRegularExpression('[0-9]{6,11}')
        validator = QRegularExpressionValidator(qreg)
        self.lineEdit_id.setEnabled(False)
        self.lineEdit_send_tel.setValidator(validator)
        self.lineEdit_hav_tel.setValidator(validator)
        self.lineEdit_id.setText(str(args[0]))
        self.lineEdit_send_name.setText(args[1])
        self.lineEdit_send_tel.setText(args[2])
        self.lineEdit_send_area.setText(args[3])
        self.lineEdit_send_address.setText(args[4])
        self.lineEdit_hav_name.setText(args[5])
        self.lineEdit_hav_tel.setText(args[6])
        self.lineEdit_hav_area.setText(args[7])
        self.lineEdit_hav_address.setText(args[8])
        for i in range(self.comboBox_goods_type.count()):
            if args[9] in self.comboBox_goods_type.itemText(i):
                self.comboBox_goods_type.setCurrentIndex(i)
                break
            if i == self.comboBox_goods_type.count() - 1:
                self.comboBox_goods_type.setCurrentIndex(i)
        self.doubleSpinBox_weight.setValue(args[10])
        self.dateTimeEdit_submit.setDateTime(args[11])

        # print(type(args[11]))
        # print(type(args[12]))
        # print(args[-3])
        if args[-3] == 0:
            self.comboBox_state.setCurrentIndex(0)
        elif args[-3] == 1:
            self.comboBox_goods_type.setEnabled(False)
            self.doubleSpinBox_weight.setEnabled(False)
            self.dateTimeEdit_sign.setDateTime(args[12])
            self.comboBox_state.setCurrentIndex(1)
        elif args[-3] == 2:
            self.comboBox_goods_type.setEnabled(False)
            self.doubleSpinBox_weight.setEnabled(False)
            self.dateTimeEdit_sign.setDateTime(args[-2])
            self.comboBox_state.setCurrentIndex(2)
        else:
            self.comboBox_goods_type.setEnabled(False)
            self.doubleSpinBox_weight.setEnabled(False)
            self.dateTimeEdit_sign.setDateTime(args[-1])
            self.comboBox_state.setCurrentIndex(3)

        self.comboBox_state.setEnabled(False)
        self.toolButton_save.clicked.connect(self.save)
        self.dateTimeEdit_submit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_sign.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_arrival.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_receipt.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_receipt.setReadOnly(True)
        self.dateTimeEdit_submit.setReadOnly(True)
        self.dateTimeEdit_sign.setReadOnly(True)
        self.dateTimeEdit_arrival.setReadOnly(True)
        self.dateTimeEdit_receipt.setEnabled(False)
        self.dateTimeEdit_submit.setEnabled(False)
        self.dateTimeEdit_sign.setEnabled(False)
        self.dateTimeEdit_arrival.setEnabled(False)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        # super().keyPressEvent(a0)
        if a0.key() == 16777220:
            self.toolButton_save.click()

    def save(self):
        new_info = (
            self.args[0], self.lineEdit_send_name.text(), self.lineEdit_send_tel.text(), self.lineEdit_send_area.text(),
            self.lineEdit_send_address.text(),
            self.lineEdit_hav_name.text(), self.lineEdit_hav_tel.text(), self.lineEdit_hav_area.text(),
            self.lineEdit_hav_address.text(),
            self.comboBox_goods_type.currentText(), self.doubleSpinBox_weight.value()
        )
        self.sql.update_bill(new_info)
        self.close()
        # pass
        # print(self.rgs)
