from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QRegularExpression, pyqtSignal, QSize
from PyQt6.QtGui import QIcon, QRegularExpressionValidator, QGuiApplication
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QToolButton, QHBoxLayout, QMessageBox, QVBoxLayout


class AuthenticationWin(QWidget):
    signal_authenticationOk = pyqtSignal(str)
    isOk = False
    signal_cancel_login = pyqtSignal()

    def __init__(self, sql):
        super().__init__()
        self.sql = sql
        self.setWindowTitle("管理员登录")
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        label1 = QLabel("管理员工号：")
        self.lineedit_username = QLineEdit()
        label2 = QLabel("管理员密码：")
        self.lineedit_password = QLineEdit()

        # reg = QRegExp('[a-zA-z0-9]+$')
        # validator = QRegExpValidator(self)
        # validator.setRegExp(reg)
        # onlyInt = QIntValidator()
        # onlyInt.setRange(0, 9223372036854775807)
        qreg = QRegularExpression('[0-9]{6,16}')
        validator = QRegularExpressionValidator(qreg)
        self.lineedit_username.setValidator(validator)
        self.lineedit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_login = QToolButton()
        self.button_login.setText("认证")
        self.button_login.setMinimumSize(111, 111)
        self.button_login.setIcon(QIcon('images/admin.png'))
        self.button_login.setIconSize(QSize(64, 64))
        self.button_login.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label1)
        hbox1.addWidget(self.lineedit_username)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(label2)
        hbox2.addWidget(self.lineedit_password)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        hbox3 = QHBoxLayout()
        hbox3.addLayout(vbox)

        hbox3.addWidget(self.button_login)
        self.setLayout(hbox3)

        self.button_login.clicked.connect(self.login)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # screen = QGuiApplication.primaryScreen().size()
        # size = self.geometry()
        # self.move(int((screen.width() - size.width()) / 2),
        #           int((screen.height() - size.height()) / 2))

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(a0)
        if a0.key() == 16777220:
            self.button_login.click()
    # print(Qt.Key.Key_Enter)

    def login(self):
        if self.lineedit_username.text() != "" and self.lineedit_password.text() != "":
            if self.sql.admin_authentication(self.lineedit_username.text(), self.lineedit_password.text()):
                # print(self.lineedit_username.text()+self.lineedit_password.text())
                self.signal_authenticationOk.emit(self.lineedit_username.text())
                self.isOk = True
                self.close()
            else:
                QMessageBox.warning(self, "错误", "工号或密码错误!")
        else:
            QMessageBox.warning(self, "错误", "工号和密码不能为空!")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        if not self.isOk:
            self.signal_cancel_login.emit()
