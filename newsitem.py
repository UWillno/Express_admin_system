from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QWidget, QLabel, QToolButton, QHBoxLayout, QMessageBox

from newsdialog import NewsDialog


class NewsItem(QListWidgetItem):

    def __init__(self, news, f):
        super().__init__()
        self.f = f
        self.sql = f.sql
        self.news = news
        self.widget = QWidget()
        label = QLabel('标题：{}\t内容：{}\t发布时间：{}'.format(news[1], news[2], news[3]))
        label.setWordWrap(True)
        self.toolbutton_news_renew = QToolButton()
        self.toolbutton_news_renew.setMinimumSize(44, 44)
        self.toolbutton_news_renew.setIcon(QIcon('images/renew.png'))
        self.toolbutton_news_renew.setIconSize(QSize(44, 44))
        self.toolbutton_news_renew.clicked.connect(self.update_news)

        self.toolbutton_news_delete = QToolButton()
        self.toolbutton_news_delete.setMinimumSize(44, 44)
        self.toolbutton_news_delete.setIcon(QIcon('images/delete.png'))
        self.toolbutton_news_delete.setIconSize(QSize(44, 44))
        self.toolbutton_news_delete.clicked.connect(self.delete_item)

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.toolbutton_news_renew)
        hbox.addWidget(self.toolbutton_news_delete)
        self.widget.setLayout(hbox)

    def delete_item(self):
        self.box = QMessageBox()
        self.box.setIcon(QMessageBox.Icon.Warning)
        self.box.setText("是否删除\"{}\"".format(self.news[1]))
        self.box.setWindowTitle("请确认！")
        self.box.addButton("确定", QMessageBox.ButtonRole.YesRole)
        self.box.addButton("取消", QMessageBox.ButtonRole.NoRole)
        self.box.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        result = self.box.exec()
        print(result)
        if int(result) == 0:
            self.sql.delete_one_news(self.news[0])
            self.f.init_page4()
        else:
            pass

    def update_news(self):
        self.dialog = NewsDialog(self.f, self.news)
        self.dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.dialog.show()
