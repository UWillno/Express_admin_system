import os.path

from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QComboBox, \
    QHBoxLayout
import sys


class Window(QObject):

    def __init__(self):
        super().__init__()

    # sys.exit(app.exec())


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("qml loader")
        self.setGeometry(200, 200, 200, 100)
        self.comboBox = QComboBox()
        for filename in os.listdir(os.getcwd()):
            if filename.split(".")[-1] == 'qml':
                self.comboBox.addItem(filename)
        self.button = QPushButton("启动")
        self.button_refresh = QPushButton("刷新")
        vbox = QVBoxLayout()
        vbox.addWidget(self.comboBox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.button_refresh)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.button.clicked.connect(lambda: self.start_qml(self.comboBox.currentText()))
        self.button_refresh.clicked.connect(self.refresh)

    def start_qml(self, qml_file=None):
        # print(qml_file)
        self.engine = QQmlApplicationEngine()

        window1 = Window()

        self.engine.rootContext().setContextProperty('window', window1)

        if qml_file and os.path.exists(qml_file):
            self.engine.load(qml_file)

    def refresh(self):
        self.comboBox.clear()
        for filename in os.listdir(os.getcwd()):
            if filename.split(".")[-1] == 'qml':
                self.comboBox.addItem(filename)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
