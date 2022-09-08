from PyQt6 import QtGui
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog

import ui_newsdialog


class NewsDialog(QDialog, ui_newsdialog.Ui_Dialog):
    def __init__(self, f, news):
        super().__init__()
        self.setupUi(self)
        self.f = f
        self.news = list(news)
        self.lineEdit.setText(news[1])
        self.textEdit.setPlainText(news[2])
        self.toolButton.setIcon(QIcon('images/book_publish_publishing_icon_220402.png'))
        self.toolButton.setIconSize(QSize(44, 44))
        self.toolButton.clicked.connect(self.submit)

    def submit(self):
        self.news[1] = self.lineEdit.text()
        self.news[2] = self.textEdit.toPlainText()
        self.f.sql.update_news(self.news)
        self.f.init_page4()
        self.close()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        # super().keyPressEvent(a0)
        if a0.key() == 16777220:
            self.toolButton.click()
