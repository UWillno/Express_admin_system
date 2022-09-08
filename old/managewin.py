from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLineEdit, QToolButton, QListWidget, QHBoxLayout, QVBoxLayout

from item import CustomItem
from sql import select_all_bills


class BillListWin(QWidget):

    def __init__(self,*args):
        super().__init__()
        self.setWindowTitle("快件编辑")

        # self.setGeometry(20, 20, 800, 900)
        self.linedit_search = QLineEdit()
        self.button_search = QToolButton()
        self.button_search.setIcon(QIcon("../images/search.png"))
        self.bill_list = QListWidget()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        hbox = QHBoxLayout()
        hbox.addWidget(self.linedit_search)
        hbox.addWidget(self.button_search)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.bill_list)

        self.setLayout(vbox)
        self.init_items()

    def init_items(self):
        self.data = select_all_bills()
        for item in self.data:
            list_item = CustomItem(*item)
            list_item.setSizeHint(QSize(800, 50))
            self.bill_list.addItem(list_item)
            self.bill_list.setItemWidget(list_item, list_item.widget)
