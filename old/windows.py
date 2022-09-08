from PyQt6.QtCore import QDateTime, QTimer
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QLabel, QWidget

from login import AuthenticationWin
from tab1 import BillAddTab
from tab2 import BillMange


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.showFullScreen()
        self.force_top()
        self.cno = ""
        self.tab_waybill_add = None
        self.tab_news_maintain = None
        self.tab_waybill_manage = None
        self.tab_news_insert = None
        self.tab_widget = None
        # self.setGeometry(-1, -1, 0, 0)
        self.login = AuthenticationWin()
        self.login.show()
        self.login.signal_authenticationOk.connect(self.create_win)
        self.login.signal_cancel_login.connect(lambda: self.close())

    def create_win(self, cno):
        # self.setVisible(True)
        self.cno = cno
        # self.setGeometry(0, 0, 1920, 1080)
        self.sizeHint()
        # self.setGeometry(0,0,400,400)
        self.setWindowTitle("管理员系统,工号:{},工作中".format(cno))

        label = QLabel("工号:{},工作中".format(cno))

        self.tab_widget = QTabWidget()
        self.tab_waybill_add = BillAddTab()
        self.tab_waybill_manage = BillMange()
        self.tab_news_insert = QWidget()
        self.tab_news_maintain = QWidget()

        self.tab_widget.addTab(self.tab_waybill_add, "快件录入")
        self.tab_widget.addTab(self.tab_waybill_manage, "快件管理")
        # self.tab_waybill_insert_ui()
        # self.addDockWidget()
        # vbox = QVBoxLayout()
        # vbox.addWidget(label)
        # vbox.addWidget(self.tab_widget)
        # self.setLayout(vbox)
        self.setCentralWidget(self.tab_widget)
        self.statusShowTime()

    def force_top(self):
        # self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.showFullScreen()

    # 获取当前时间 该部分来自csdn@胜天半月子，仅针对pyqt6微调
    def showCurrentTime(self, timeLabel):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # print(timeDisplay)
        # 状态栏显示
        timeLabel.setText(timeDisplay)

    def statusShowTime(self):
        self.timer = QTimer()
        self.timeLabel = QLabel()
        self.statusBar().addPermanentWidget(self.timeLabel, 1)
        self.timer.timeout.connect(lambda: self.showCurrentTime(self.timeLabel))  # 这个通过调用槽函数来刷新时间

        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms  即1s
