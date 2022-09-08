# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_packages_insert = QtWidgets.QWidget()
        self.tab_packages_insert.setObjectName("tab_packages_insert")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_packages_insert)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.tab_packages_insert)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_packages_insert)
        self.lineEdit_11.setStyleSheet("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_3.addWidget(self.lineEdit_11)
        self.toolButton = QtWidgets.QToolButton(self.tab_packages_insert)
        self.toolButton.setMinimumSize(QtCore.QSize(111, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_packages_insert)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_packages_insert, "")
        self.tab_packages_manage = QtWidgets.QWidget()
        self.tab_packages_manage.setObjectName("tab_packages_manage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_packages_manage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_packages_manage)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton_search = QtWidgets.QToolButton(self.tab_packages_manage)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_search.setIcon(icon1)
        self.toolButton_search.setObjectName("toolButton_search")
        self.horizontalLayout.addWidget(self.toolButton_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.tab_packages_manage)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_modify = QtWidgets.QToolButton(self.tab_packages_manage)
        self.toolButton_modify.setMinimumSize(QtCore.QSize(111, 111))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/addd.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_modify.setIcon(icon2)
        self.toolButton_modify.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_modify.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_modify.setObjectName("toolButton_modify")
        self.horizontalLayout_2.addWidget(self.toolButton_modify)
        self.toolButton_remove = QtWidgets.QToolButton(self.tab_packages_manage)
        self.toolButton_remove.setMinimumSize(QtCore.QSize(111, 111))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/remove.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_remove.setIcon(icon3)
        self.toolButton_remove.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_remove.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_remove.setObjectName("toolButton_remove")
        self.horizontalLayout_2.addWidget(self.toolButton_remove)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_packages_manage, "")
        self.tab_news_insert = QtWidgets.QWidget()
        self.tab_news_insert.setObjectName("tab_news_insert")
        self.tabWidget.addTab(self.tab_news_insert, "")
        self.tab_news_mantain = QtWidgets.QWidget()
        self.tab_news_mantain.setObjectName("tab_news_mantain")
        self.tabWidget.addTab(self.tab_news_mantain, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理员系统"))
        self.label_10.setText(_translate("MainWindow", "运单号："))
        self.toolButton.setText(_translate("MainWindow", "录入"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "待录入运单号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "寄件人"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "寄件人电话"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "寄件地址"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "收件人"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "收件人电话"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "收件地址"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_packages_insert), _translate("MainWindow", "快件录入"))
        self.toolButton_search.setText(_translate("MainWindow", "..."))
        self.toolButton_modify.setText(_translate("MainWindow", "修改"))
        self.toolButton_remove.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_packages_manage), _translate("MainWindow", "快件管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_news_insert), _translate("MainWindow", "新闻发布"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_news_mantain), _translate("MainWindow", "新闻维护"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
