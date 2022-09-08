from PyQt6 import QtGui
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QAbstractItemView, QTableWidgetItem, QMenu, \
    QMessageBox, QInputDialog, QLineEdit

from insertdialog import InsertDialog
from item import BillItem
from login import AuthenticationWin
from newsitem import NewsItem
from sql import SQL
# import sql
from threads import Page0Thread, TableThread, BillsListThread
from ui_system import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.can_exit = 0
        self.timer = None
        self.timeLabel = None
        self.logout_dialog = None
        self.cno = None
        self.insert_dialog = None
        self.login_widget = None
        self.page2thread = None
        self.table_thread = None
        self.sign_menu = None
        self.all_bills_list = None
        self.page0thread = None
        self.page0_hbox = None
        self.chart_view = None
        self.chart = None
        self.setupUi(self)

        self.sql = SQL('192.168.111.111', 'root', '0125', 'express')
        # self.sql = SQL('localhost', 'root', '123456', 'express')

        self.show_login()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        if self.can_exit != 1:
            a0.ignore()

    def show_login(self):
        self.force_top()
        self.login_widget = AuthenticationWin(self.sql)
        self.login_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.login_widget.show()
        self.login_widget.signal_cancel_login.connect(self._exit)
        self.login_widget.signal_authenticationOk.connect(self.login_success)

    def _exit(self):
        self.can_exit = 1
        self.close()

    def login_success(self, cno):
        self.cno = cno
        self.create_win()

    def create_win(self):
        # self.tableWidget_bills = None
        self.status_show_time()
        self.init_page0(self.sql.select_allstate())
        self.init_table()
        self.init_page2()
        self.init_page4()
        self.sign_menu = QMenu()
        self.sign_menu.addAction(QIcon('images/insert.png'), "手动录入", self.insert_one)
        self.toolButton_deal.setMenu(self.sign_menu)
        self.toolButton_search.clicked.connect(self.search_bills)

        self.action_view.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.action_sign.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.action_update.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.action_postnews.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.action_newsupdate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.action_newsupdate.triggered.connect(self.init_page4)
        self.radioButton_waittosign.clicked.connect(lambda: self.init_table(0))
        self.radioButton_waittoarrival.clicked.connect(lambda: self.init_table(1))
        self.radioButton_waittoreceipt.clicked.connect(lambda: self.init_table(2))

        self.table_thread = TableThread(self.sql.select_all_state_to(0), self)
        self.table_thread.table_signal.connect(self.init_table)
        self.stackedWidget.setCurrentIndex(0)
        # self.action_run.triggered.connect(self.close)
        # self.radiotimer()
        self.table_thread.start()
        # print(self.radioButton_waittosign.isChecked())
        self.page2thread = BillsListThread(self.sql.select_all_bills(), self.sql)
        self.page2thread.list_changed_signal.connect(self.search_bills)
        self.page2thread.start()

        self.toolButton_deal.clicked.connect(self.bills_state_change)
        self.toolButton_newspost.clicked.connect(self.insert_news)

        self.action_run.triggered.connect(self.logout)

        self.listWidget_bills.itemDoubleClicked.connect(lambda item: item.update_button.click())
        self.listWidget_news.itemDoubleClicked.connect(lambda item: item.toolbutton_news_renew.click())

        # .triggered.connect(lambda : print("hello world"))

    def logout(self):
        self.logout_dialog = QInputDialog()
        self.logout_dialog.setWindowTitle("工号：{}登出".format(self.cno))
        self.logout_dialog.setLabelText("请输入密码：")
        self.logout_dialog.setOkButtonText("确定")
        self.logout_dialog.setCancelButtonText("取消")
        self.logout_dialog.setTextEchoMode(QLineEdit.EchoMode.Password)
        self.logout_dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        if self.logout_dialog.exec() == 1 and self.sql.admin_authentication(self.cno,
                                                                            str(self.logout_dialog.textValue())):
            self._exit()

    def insert_news(self):
        # if self.lineEdit_newstitle.text().strip(" ") != "" and self.textEdit_newscontext.toPlainText().strip(" ") == "":
        news = ()
        if self.lineEdit_newstitle.text() != "" and self.textEdit_newscontext.toPlainText() != "":
            news = (self.lineEdit_newstitle.text(), self.textEdit_newscontext.toPlainText())
            self.sql.insert_news(news)
            self.lineEdit_newstitle.setText('')
            self.textEdit_newscontext.setText('')
            QMessageBox.information(self, "通知", "新闻发布成功！")

    def insert_one(self):
        self.insert_dialog = InsertDialog(self.sql)
        self.insert_dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.insert_dialog.show()

    def init_page0(self, data):
        if self.chart is None:
            # data=self.sql.select_allstate()
            self.chart = QChart()
            self.chart_view = QChartView()
            self.chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
            self.chart.setTitle("当前快件状态")
            # self.chart.setFont(QFont("Times",24))
            self.chart.setTheme(QChart.ChartTheme.ChartThemeQt)
            # chart.legend().setVisible(False)
            self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
            self.chart.setTitleFont(QFont('Microsoft YaHei UI', 20))
            self.chart.legend().setFont(QFont('Microsoft YaHei UI', 14))
            self.chart_view.setChart(self.chart)
            self.page0thread = Page0Thread(data, self.sql)
            self.page0thread.pie_chart_signal.connect(self.init_page0)
            self.page0thread.start()

        self.chart.removeAllSeries()
        series = QPieSeries()
        # series.setHoleSize(0.2)
        data = str(data)
        pie1, pie2, pie3, pie4 = data.count("0"), data.count('1'), data.count('2'), data.count('3')
        series.append("待发货：{}".format(pie1), pie1)
        series.append("待入站：{}".format(pie2), pie2)
        series.append("待签收：{}".format(pie3), pie3)
        series.append("已签收:{}".format(pie4), pie4)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
        series.setHoleSize(0.4)

        self.chart.addSeries(series)
        if self.page0_hbox is None:
            self.page0_hbox = QHBoxLayout()
            self.page0_hbox.addWidget(self.chart_view)
            self.page.setLayout(self.page0_hbox)

        # self.setCentralWidget(chart_view)

    def init_table(self, num=0, data=None):
        # print(num)
        # print(data)

        if data is None:
            data = self.sql.select_all_state_to(num)
            # print(data)
            self.tableWidget_bills.horizontalHeader().setStretchLastSection(True)
            self.tableWidget_bills.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑

        # 数据行数大于表行
        # if len(data) != self.table.rowCount():
        for i in range(self.tableWidget_bills.rowCount()):
            self.tableWidget_bills.removeRow(i)
        # if data:
        self.tableWidget_bills.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(11):
                if j == 0:
                    item = QTableWidgetItem(str(data[i][j]))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.tableWidget_bills.setItem(i, j, item)
                else:
                    self.tableWidget_bills.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def force_top(self):
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.showFullScreen()

    # 获取当前时间 该部分来自csdn@胜天半月子，仅针对pyqt6微调
    def show_current_time(self, time_label):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        time_display = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # print(timeDisplay)
        # 状态栏显示
        time_label.setText(time_display)

    def status_show_time(self):
        self.timer = QTimer()
        self.timeLabel = QLabel()
        self.statusBar().addPermanentWidget(self.timeLabel, 0)
        self.timer.timeout.connect(lambda: self.show_current_time(self.timeLabel))  # 这个通过调用槽函数来刷新时间

        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms  即1s

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.stackedWidget.currentIndex() == 1:
            if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                for row in range(self.tableWidget_bills.rowCount()):
                    self.tableWidget_bills.item(row, 0).setCheckState(Qt.CheckState.Checked)
            elif event.modifiers() == Qt.KeyboardModifier.AltModifier:
                for row in range(self.tableWidget_bills.rowCount()):
                    self.tableWidget_bills.item(row, 0).setCheckState(Qt.CheckState.Unchecked)

    def bills_state_change(self):
        bills_tuple = set()
        # self.qthread.sleep(1)
        for row in range(self.tableWidget_bills.rowCount()):
            if self.lineEdit_billid.text() == self.tableWidget_bills.item(row, 0).text():
                bills_tuple.add(str(self.lineEdit_billid.text()))
                self.lineEdit_billid.setText("")
                continue
            # print(self.table.rowCount())
            if self.tableWidget_bills.item(row, 0).checkState() == Qt.CheckState.Checked:
                bill_id = self.tableWidget_bills.item(row, 0).text()
                bills_tuple.add(str(bill_id))
        bills_tuple = tuple(bills_tuple)
        # print(bills_tuple)
        if self.radioButton_waittosign.isChecked():
            self.sql.state_change(0, bills_tuple)
        elif self.radioButton_waittoarrival.isChecked():
            self.sql.state_change(1, bills_tuple)
        elif self.radioButton_waittoreceipt.isChecked():
            self.sql.state_change(2, bills_tuple)

        # if len(add_list) >= 1:
        # if not enter_bills(add_list):
        # QMessageBox.warning(self, "异常", "数据库异常")

    def init_page2(self):
        # def init_items(self, data=select_all_bills(), flag=0):
        self.listWidget_bills.clear()
        self.all_bills_list = self.sql.select_all_bills()
        # if flag == 0:
        #     self.current_items = []

        for item in self.all_bills_list:
            list_item = BillItem(self.sql, *item)
            # list_item.setSizeHint(QSize(800, 50))
            # self.listWidget_bills.setResizeMode(QListView.ResizeMode.Adjust)
            list_item.setSizeHint(list_item.widget.sizeHint())
            self.listWidget_bills.addItem(list_item)
            self.listWidget_bills.setItemWidget(list_item, list_item.widget)

        # if flag == 0:
        #     self.current_items.append(list_item)
        # print(self.current_items)

    def search_bills(self):
        self.toolButton_search.setEnabled(False)
        QTimer.singleShot(1000, lambda: self.toolButton_search.setEnabled(True))
        self.listWidget_bills.clear()
        self.all_bills_list = self.sql.select_all_bills()
        search_list = []
        if self.lineEdit_search.text() == "":
            self.init_page2()
            return
        else:
            text = self.lineEdit_search.text()
            # print(self.all_bills_list)
            for item in self.all_bills_list:
                if text in str(item):
                    search_list.append(item)

        if search_list:
            for item in search_list:
                list_item = BillItem(self.sql, *item)
                # self.listWidget_bills.setResizeMode(QListView.ResizeMode.Adjust)
                list_item.setSizeHint(list_item.widget.sizeHint())

                # list_item.setSizeHint(QSize(800, 50))
                self.listWidget_bills.addItem(list_item)
                self.listWidget_bills.setItemWidget(list_item, list_item.widget)

    def init_page4(self):
        self.listWidget_news.clear()
        old_news = self.sql.select_all_news()
        # self.listWidget_news.setItemWidget()
        for i in old_news:
            item = NewsItem(i, self)
            # item.setSizeHint(QSize(800, 50)
            item.setSizeHint(item.widget.sizeHint())
            self.listWidget_news.addItem(item)
            self.listWidget_news.setItemWidget(item, item.widget)
    # def refresh_bills_list_widget(self):
    #     if self.lineEdit_search.text() == "":
    #         self.init_page2()
    #     else:
    #         self.
