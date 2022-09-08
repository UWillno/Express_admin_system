from operator import eq

from PyQt6.QtCore import QThread, pyqtSignal

import sql


class Page0Thread(QThread):
    pie_chart_signal = pyqtSignal(object)

    def __init__(self, data, sql):
        super().__init__()
        self.data = data
        self.sql = sql

    def run(self):
        while True:
            temp = self.sql.select_allstate()
            if not temp:
                continue
            if str(temp) != str(self.data):
                self.data = temp
                self.pie_chart_signal.emit(self.data)
            self.msleep(44)


class TableThread(QThread):
    table_signal = pyqtSignal(int)

    def __init__(self, data, f):
        super().__init__()
        self.data = data
        self.f = f
        # self.num = 0

    def run(self):
        while True:
            # self.radioButton_waittosign.clicked.connect(lambda: self.init_table(0))
            # self.radioButton_waittoarrival.clicked.connect(lambda: self.init_table(1))
            # self.radioButton_waittoreceipt.clicked.connect(lambda: self.init_table(2))
            num = 0
            if self.f.radioButton_waittoreceipt.isChecked():
                num = 2
            elif self.f.radioButton_waittoarrival.isChecked():
                num = 1
            elif self.f.radioButton_waittosign.isChecked():
                num = 0
            data = self.f.sql.select_all_state_to(num)
            if not eq(data, self.data):
                self.data = data
                self.table_signal.emit(num)
            self.msleep(44)

            # temp = sql.select_allstate()
            # if str(temp)!=str(self.data):
            #     self.data = temp
            #     self.pie_chart_signal.emit(self.data)


class BillsListThread(QThread):
    list_changed_signal = pyqtSignal()

    def __init__(self, current_list, sql):
        super().__init__()
        self.current_list = current_list
        self.sql = sql

    def run(self):
        while True:
            current_list = self.sql.select_all_bills()
            if not eq(self.current_list, current_list):
                self.current_list = current_list
                self.list_changed_signal.emit()
            self.msleep(44)
