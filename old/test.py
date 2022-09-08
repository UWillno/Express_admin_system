# def a(*args):
#     print(args[0])
#
#
# a(*(1, "23", "sadfasf", 432))
from datetime import datetime, time

from PyQt6.QtCore import QDate, QDateTime

# QtSql
print(datetime.now().second)

# sql = "UPDATE delivery SET send_name='{1}', send_tel='{2}' ,send_area='{3}' ,send_address='{4}' ,hav_name='{5}', hav_tel='{6}', hav_area='{7}' ,hav_address='{8}' ,goods_type='{9}' ,weight='{10}' ,commit_time='{11}',sign_time='{12}',arrival_state={13},sign_state={14} WHERE id={0}"
# args=(2,3,4,5,6,"asd","asd","asd",4,1,1,1,1,1,1)
# print(sql.format(*args))
# print(QDateTime().currentDateTimeUtc()

