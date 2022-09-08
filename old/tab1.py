import mysql
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QToolButton, QHBoxLayout, QVBoxLayout, QTableWidget, \
    QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from mysql.connector import errors
from PyQt6.QtGui import QKeyEvent
from sql import select_allstate, enter_bills
from threads import QThreadTAB1


class BillAddTab(QWidget):

    def __init__(self):
        super().__init__()
        self.table = None
        label = QLabel("运单号：")
        self.lineedit_id = QLineEdit()
        self.button_add = QToolButton()
        self.button_add.setIcon(QIcon('../images/add.png'))
        self.button_add.setText("添加")
        self.button_add.setMinimumSize(111, 111)
        self.button_add.setIconSize(QSize(64, 64))
        self.button_add.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.button_add.setVisible(True)

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.lineedit_id)
        hbox.addWidget(self.button_add)
        vbox = QVBoxLayout()
        self.init_table()
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

        self.qthread = QThreadTAB1(self, select_allstate())
        self.qthread.update_signal.connect(self.init_table)
        self.qthread.start()
        self.button_add.clicked.connect(self.bills_add)

    def init_table(self, data=None):
        # print("初始化")
        # if self.table is not None:
        #     self.table.clear()
        if data is None:
            data = select_allstate()
            # if type(data)!='mysql.connector.errors':
            if isinstance(data, list):
                print(data)
                if self.table is None:
                    self.table = QTableWidget(len(data), 12)
                    col_name = ['运单号', '寄件人', '电话', '所在区域', '详细地址', '收件人', '电话', '所在区域',
                                '详细地址',
                                '快件类型', '快件重量(KG)', '提交时间']
                    self.table.setHorizontalHeaderLabels(col_name)
                    # self.table.setStyleSheet(
                    #     'QAbstractItemView::indicator {width：0px; height:0px;} QTableWidget::item{width:500px;height:40px;}')
                    # 不生效？？

        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑
        # 数据行数大于表行
        # if len(data) != self.table.rowCount():
        self.table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(12):
                if j == 0:
                    item = QTableWidgetItem(str(data[i][j]))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.table.setItem(i, j, item)
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        # print(data)

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            for row in range(self.table.rowCount()):
                self.table.item(row, 0).setCheckState(Qt.CheckState.Checked)
        elif event.modifiers() == Qt.KeyboardModifier.AltModifier:
            for row in range(self.table.rowCount()):
                self.table.item(row, 0).setCheckState(Qt.CheckState.Unchecked)

    def bills_add(self):
        add_list = set()
        # self.qthread.sleep(1)
        for row in range(self.table.rowCount()):
            if self.lineedit_id.text() == self.table.item(row, 0).text():
                add_list.add(str(self.lineedit_id.text()))
                self.lineedit_id.setText("")
                continue
            # print(self.table.rowCount())
            if self.table.item(row, 0).checkState() == Qt.CheckState.Checked:
                bill_id = self.table.item(row, 0).text()
                add_list.add(str(bill_id))
        add_list = tuple(add_list)
        if len(add_list) >= 1:
            if not enter_bills(add_list):
                QMessageBox.warning(self, "异常", "数据库异常")
