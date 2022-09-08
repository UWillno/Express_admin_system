from PyQt6.QtCharts import QChart, QPieSeries, QChartView
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QToolButton, QHBoxLayout, QLineEdit, QListWidget, QDialog

from item import CustomItem
from itemdialog import ItemDialog
from managewin import BillListWin
from sql import chart_data, select_all_bills
from threads import QThreadChart, QThreadBillList


class BillMange(QWidget):

    def __init__(self):
        super().__init__()
        self.item_dialog = None
        self.current_items = []
        self.data = None
        self.manage_widget = None
        self.chart_view = None
        self.chart = None
        self.init_pie_chart()

        self.button_update = QToolButton()
        self.button_remove = QToolButton()
        # self.button_search = QToolButton()

        self.button_update.setIcon(QIcon('../images/renew.png'))
        self.button_update.setIconSize(QSize(64, 64))
        self.button_update.setMinimumSize(QSize(111, 111))
        self.button_update.setText("编辑")
        self.button_update.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # self.button_update.clicked.connect(self.bill_manage)

        self.button_remove.setIcon(QIcon('../images/remove.png'))
        self.button_remove.setIconSize(QSize(64, 64))
        self.button_remove.setMinimumSize(QSize(111, 111))
        self.button_remove.setText("删除")
        self.button_remove.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.linedit_search = QLineEdit()
        self.button_search = QToolButton()
        self.button_search.setIcon(QIcon("../images/search.png"))
        self.button_search.setIconSize(QSize(44, 44))
        self.bill_list = QListWidget()

        # Layout
        # 按钮
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.button_update)
        hbox_buttons.addWidget(self.button_remove)

        # 搜索栏
        hbox_search = QHBoxLayout()
        hbox_search.addWidget(self.linedit_search)
        hbox_search.addWidget(self.button_search)

        # 右
        vbox_right = QVBoxLayout()
        vbox_right.addLayout(hbox_search)
        vbox_right.addWidget(self.bill_list)
        vbox_right.addLayout(hbox_buttons)

        # 左
        vbox_left = QVBoxLayout()
        vbox_left.addWidget(self.chart_view)
        # 全局

        hbox_all = QHBoxLayout()
        hbox_all.addLayout(vbox_left)
        hbox_all.addLayout(vbox_right)
        self.setLayout(hbox_all)

        self.init_items()
        x, y, z = chart_data()
        self.qthread_chart = QThreadChart(self, "{}{}{}".format(x, y, z))
        self.qthread_chart.chart_update_signal.connect(self.init_pie_chart)

        self.qthread_list = QThreadBillList(self, select_all_bills())
        self.qthread_list.bills_update_signal.connect(self.init_items)

        self.qthread_chart.start()
        self.qthread_list.start()

        self.button_update.clicked.connect(self.manage_bill)

        self.button_search.clicked.connect(self.search_all)
        self.linedit_search.returnPressed.connect(self.search_all)
        # self.button_search.

    def init_pie_chart(self):
        if self.chart is None:
            self.chart = QChart()
            self.chart_view = QChartView()
            self.chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
            self.chart.setTitle("当前快件状态")
            self.chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)
            # chart.legend().setVisible(False)
            self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
            self.chart_view.setChart(self.chart)

        self.chart.removeAllSeries()

        series = QPieSeries()
        # series.setHoleSize(0.2)

        pie1, pie2, pie3 = chart_data()
        series.append("待录入：{}".format(pie1), pie1)
        series.append("运输中：{}".format(pie2), pie2)
        series.append("已签收：{}".format(pie3), pie3)
        # series.slices()[0].setLabelFont(QFont("Times", 44))
        my_slice = series.slices()[0]
        my_slice.setExploded(True)
        series.setLabelsVisible(True)

        # series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)
        my_slice.setLabelVisible(True)

        self.chart.addSeries(series)

        # self.setCentralWidget(chart_view)

    def bill_manage(self):
        self.manage_widget = BillListWin()
        self.manage_widget.show()

    def init_items(self, data=select_all_bills(), flag=0):
        self.bill_list.clear()
        self.data = data
        # if flag == 0:
        #     self.current_items = []

        for item in self.data:
            list_item = CustomItem(*item)
            list_item.setSizeHint(QSize(800, 50))
            self.bill_list.addItem(list_item)
            self.bill_list.setItemWidget(list_item, list_item.widget)
            if flag == 0:
                self.current_items.append(list_item)
            # print(self.current_items)

    def search_all(self):
        # print(self.current_items[0].info)
        if self.linedit_search.text() == "":
            self.init_items([item.info for item in self.current_items], 1)
        else:
            temp = []
            text = self.linedit_search.text()
            for item in self.current_items:
                if text in str(item.info):
                    temp.append(item.info)
            self.init_items(temp, 1)
            # for i in range(self.bill_list.count()):
            #     if text in str(self.bill_list.item(i).info):
            #         pass
            #     else:
            #         self.bill_list.removeItemWidget(self.bill_list.item(i))

    def manage_bill(self):
        if self.bill_list.currentItem() is not None:
            self.item_dialog = ItemDialog(*self.bill_list.currentItem().info)
            self.item_dialog.show()

            print(self.bill_list.currentItem().info)
