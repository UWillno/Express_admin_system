# 这是一个示例 Python 脚本。
from PyQt6.QtGui import QIcon
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from PyQt6.QtWidgets import QApplication, QWidget, QStyle, QStyleFactory
import sys

from SystemMainWindow import MainWindow

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('images/Icon.png'))

    app.setStyle(QStyleFactory.create("Fusion"))
    # app.setStyle(QStyleFactory.create("windowsvista"))
    # print(QStyleFactory.keys())

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
