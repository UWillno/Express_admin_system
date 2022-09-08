from PyQt6.QtWidgets import QListWidgetItem, QLabel, QWidget, QVBoxLayout


class CustomItem(QListWidgetItem):
    # def __init__(self, bill_id, send_name, send_tel, send_area, send_address, hav_name, hav_tel, hav_area, hav_address,
    #              weight, commit_time, sign_time, arrival_state, sign_state):
    def __init__(self, *args):
        super().__init__()
        self.widget = QWidget()
        self.info = args
        s = "运单号：{}\t{}\t->\t{}\t{}{}\t->\t{}{}\t{}\t{}KG\t".format(self.info[0], self.info[3], self.info[7],
                                                                       self.info[
                                                                           1], self.info[2], self.info[5], self.info[6],
                                                                       self.info[9], self.info[10])
        self.label = QLabel(s)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.widget.setLayout(vbox)
