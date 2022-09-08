from PyQt6.QtCore import QSize, pyqtSignal, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QLabel, QWidget, QToolButton, QHBoxLayout, QMessageBox

from billdialog import BillItemDialog


class BillItem(QListWidgetItem):
    # def __init__(self, bill_id, send_name, send_tel, send_area, send_address, hav_name, hav_tel, hav_area, hav_address,
    #              weight, commit_time, sign_time, arrival_state, sign_state):
    def __init__(self, sql, *args):
        super().__init__()
        self.remove_item_signal = pyqtSignal(str)
        self.sql = sql
        self.widget = QWidget()
        self.info = args
        s = "运单号：{}\t{}\t->\t{}\t{}({})\t->\t{}({})\t{}\t{}KG\t".format(self.info[0], self.info[3], self.info[7],
                                                                           self.info[
                                                                               1], self.info[2], self.info[5],
                                                                           self.info[6],
                                                                           self.info[9], self.info[10])
        self.label = QLabel(s)
        self.label.setWordWrap(True)
        self.update_button = QToolButton()
        self.update_button.setIcon(QIcon('images/renew.png'))
        self.update_button.setIconSize(QSize(44, 44))
        self.remove_button = QToolButton()
        self.remove_button.setIcon(QIcon('images/remove.png'))
        self.remove_button.setIconSize(QSize(44, 44))
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.update_button)
        hbox.addWidget(self.remove_button)
        # vbox = QVBoxLayout()
        # vbox.addWidget(self.label)
        self.widget.setLayout(hbox)
        self.update_button.clicked.connect(self.show_dialog)
        self.remove_button.clicked.connect(self.delete_item)



    def show_dialog(self):
        self.dialog = BillItemDialog(self.sql, *self.info)
        self.dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.dialog.show()

    def delete_item(self):
        self.box = QMessageBox()
        self.box.setIcon(QMessageBox.Icon.Warning)
        self.box.setText("是否删除运单号为{}的快件？".format(self.info[0]))
        self.box.setWindowTitle("请确认！")
        self.box.addButton("确定", QMessageBox.ButtonRole.YesRole)
        self.box.addButton("取消", QMessageBox.ButtonRole.NoRole)
        self.box.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        result = self.box.exec()
        print(result)
        if int(result) == 0:
            self.sql.delete_one_bill(self.info[0])
        else:
            pass
