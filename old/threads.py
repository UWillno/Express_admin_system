from operator import eq

from PyQt6.QtCore import QThread, pyqtSignal

from sql import select_allstate, chart_data, select_all_bills


class QThreadTAB1(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, tab, result):
        super().__init__()
        self.tab = tab
        self.result = result

    def run(self):
        while True:
            # print("循环")
            result1 = select_allstate()
            if not eq(self.result, result1):
                self.result = result1
                # print(result)
                self.update_signal.emit(self.result)
                print("信号发射")


class QThreadChart(QThread):
    chart_update_signal = pyqtSignal()

    def __init__(self, tab, data):
        super().__init__()
        self.tab = tab
        self.data = data

    def run(self):
        while True:
            # print("循环")
            x, y, z = chart_data()
            if x is not None and y is not None and z is not None:
                if not eq("{}{}{}".format(x, y, z), self.data):
                    self.data = "{}{}{}".format(x, y, z)
                    self.chart_update_signal.emit()
            # self.sleep(4)


class QThreadBillList(QThread):
    bills_update_signal = pyqtSignal(object)

    def __init__(self, tab, data):
        super().__init__()
        self.tab = tab
        self.data = data

    def run(self):
        while True:
            # print("循环")
            temp = select_all_bills()
            if not eq(temp, self.data):
                self.bills_update_signal.emit(temp)
                self.data = temp
