import mysql.connector as mc


class SQL:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        #  = "192.168.1.217"
        # user = "root"
        # password = "0125"
        # database = "express"

    def select_allstate(self):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            cursor.execute('SELECT arrival_state FROM delivery')
            result = cursor.fetchall()
            cursor.close()
            mydb.close()
            return result
        except mc.Error as e:
            print(e)
            return False

    def select_all_state_to(self, num):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            cursor.execute('SELECT * FROM delivery where arrival_state={} '.format(num))
            result = cursor.fetchall()
            cursor.close()
            mydb.close()
            return result
        except mc.Error as e:
            print(e)
            return False

    def state_change(self, num, bills_tuple):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            if num == 0:
                if len(bills_tuple) > 1:
                    cursor.execute(
                        'UPDATE delivery SET sign_time = NOW(), arrival_state = 1 WHERE id in {}'.format(bills_tuple))
                elif len(bills_tuple) == 1:
                    cursor.execute(
                        'UPDATE delivery SET sign_time = NOW(), arrival_state = 1 WHERE id ={}'.format(bills_tuple[0]))
            elif num == 1:
                if len(bills_tuple) > 1:
                    cursor.execute(
                        'UPDATE delivery SET arrival_time=NOW(),arrival_state=2 WHERE id in {}'.format(bills_tuple))
                elif len(bills_tuple) == 1:
                    cursor.execute(
                        'UPDATE delivery SET arrival_time=NOW(),arrival_state=2 WHERE id ={}'.format(bills_tuple[0]))
            else:
                if len(bills_tuple) > 1:
                    cursor.execute(
                        'UPDATE delivery SET receipt_time=NOW(),arrival_state=3 WHERE id in {}'.format(bills_tuple))
                elif len(bills_tuple) == 1:
                    cursor.execute(
                        'UPDATE delivery SET receipt_time=NOW(),arrival_state=3 WHERE id ={}'.format(bills_tuple[0]))
            mydb.commit()
            cursor.close()
            mydb.close()
            # return True
        except mc.Error as e:
            print(e)
            # return False

    def select_all_bills(self):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM delivery")
            result = cursor.fetchall()
            cursor.close()
            # print(result)
            return result
        except mc.Error as e:
            print(e)

    def update_bill(self, info):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = "UPDATE delivery SET send_name = '{1}',send_tel = '{2}',send_area = '{3}',send_address = '{4}',hav_name = '{5}',hav_tel = '{6}',hav_area = '{7}',hav_address = '{8}',goods_type = '{9}',weight = {10} WHERE id = {0}".format(
                *info)
            # cursor.execute(
            # )
            print(sql)
            cursor.execute(sql)
            mydb.commit()
            cursor.close()
            mydb.close()
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def delete_one_bill(self, bill_id):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM delivery WHERE id = {}".format(bill_id))
            mydb.commit()
            cursor.close()
            mydb.close()
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def insert_bill(self, info):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = ""
            if info[-3] == 0:
                sql = "INSERT into delivery VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', {}, {}, {}, {})".format(
                    *info)
            elif info[-3] == 1:
                sql = "INSERT into delivery VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, {}, {})".format(
                    *info)
            elif info[-3] == 2:
                sql = "INSERT into delivery VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, '{}', {})".format(
                    *info)
            elif info[-3] == 3:
                sql = "INSERT into delivery VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, '{}', {}')".format(
                    *info)
            print(sql)
            cursor.execute(sql)
            mydb.commit()
            cursor.close()
            mydb.close()
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def insert_news(self, news):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = "INSERT INTO news VALUES(0,'{}','{}',NOW())".format(*news)
            # print(sql)
            cursor.execute(sql)
            mydb.commit()
            cursor.close()
            mydb.close()
        except mc.Error as e:
            print(e)

    def select_all_news(self):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = "SELECT * FROM news"
            # print(sql)
            cursor.execute(sql)
            # mydb.commit()
            result = cursor.fetchall()
            cursor.close()
            mydb.close()
            return result
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def delete_one_news(self, news_id):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = "DELETE FROM news WHERE id = {}".format(news_id)
            # print(sql)
            cursor.execute(sql)
            # mydb.commit()
            mydb.commit()
            cursor.close()
            mydb.close()
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def update_news(self, news):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            print(news)
            sql = "UPDATE news set title='{1}',content='{2}' WHERE id={0}".format(news[0], news[1], news[2])

            print(sql)
            cursor.execute(sql)
            mydb.commit()
            cursor.close()
            mydb.close()
            # print(result)
            # return result
        except mc.Error as e:
            print(e)

    def admin_authentication(self, cno=0, pwd=''):
        try:
            mydb = mc.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            cursor.execute("SELECT EXISTS(SELECT * FROM `admin` WHERE cno={} and pwd=MD5('{}'))".format(cno, pwd))
            result = cursor.fetchone()[0]
            cursor.close()
            # print(result)
            if result == 1:
                return True
            else:
                return False
            # print(result)
            # print(type(result))
        except mc.Error as e:
            print(e)
            return False

# print(str(select_allstate()).count('1'))

# select_unentered_bills = "select * from delivery where sign_time is NULL"


# def unentered_bills():
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute(select_unentered_bills)
#         result = cursor.fetchall()
#         cursor.close()
#         return result
#     except mc.Error as e:
#         return e
#
#
# def admin_authentication(cno=0, pwd=""):
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute("SELECT EXISTS(SELECT * FROM `admin` WHERE cno={} and pwd=MD5('{}'))".format(cno, pwd))
#         result = cursor.fetchone()[0]
#         cursor.close()
#         print(result)
#
#         if result == 1:
#             return True
#         else:
#             return False
#         # print(result)
#         # print(type(result))
#     except mc.Error as e:
#         print(mc.Error)
#         return e
#
#
# def enter_bills(bills_list):
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         if len(bills_list) == 1:
#             # print(bills_list[0])
#             cursor.execute("UPDATE delivery set sign_time=NOW() WHERE id={}".format(bills_list[0]))
#         elif len(bills_list) > 1:
#             cursor.execute("UPDATE delivery set sign_time=NOW() WHERE id in {}".format(bills_list))
#         # print("UPDATE delivery set sign_time=NOW() WHERE id=%s".format(bill_id))
#         # result = cursor.fetchone()
#         # print(result)
#         # if result:
#         #     cursor.close()
#         mydb.commit()
#         cursor.close()
#         return True
#     except mc.Error as e:
#         print(e)
#         return False
#
#
# def chart_data():
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute("SELECT COUNT(*) FROM delivery WHERE sign_time is NULL")
#         count_waiting = cursor.fetchone()[0]
#         cursor.execute("SELECT COUNT(*) FROM delivery WHERE arrival_state !=0")
#         count_arriving = cursor.fetchone()[0]
#         cursor.execute("SELECT COUNT(*) FROM delivery WHERE sign_state !=0")
#         count_arrived = cursor.fetchone()[0]
#
#         return count_waiting, count_arriving, count_arrived
#
#         # print(result[0])
#         return True
#     except mc.Error as e:
#         print(mc.Error)
#         return e
#
#
# def select_all_bills():
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute("SELECT * FROM delivery")
#         result = cursor.fetchall()
#         return result
#     except mc.Error as e:
#         print(mc.Error)
#         return e
#
#
# def update_one_bills(*args):
#     try:
#         if eq(args[12], 'DEFAULT'):
#             sql = "UPDATE delivery SET id = {}, send_name='{}', send_tel='{}' ,send_area='{}' ,send_address='{}' ,hav_name='{}', hav_tel='{}', hav_area='{}' ,hav_address='{}' ,goods_type='{}' ,weight='{}' ,commit_time='{}',sign_time={},arrival_state={},sign_state={} WHERE id={}"
#             sql = sql.format(args)
#         else:
#             sql = "UPDATE delivery SET id = {}, send_name='{}', send_tel='{}' ,send_area='{}' ,send_address='{}' ,hav_name='{}', hav_tel='{}', hav_area='{}' ,hav_address='{}' ,goods_type='{}' ,weight='{}' ,commit_time='{}',sign_time='{}',arrival_state={},sign_state={} WHERE id={}"
#             sql = sql.format(args)
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute(sql)
#         cursor.commit()
#         return True
#     except mc.Error as e:
#         print(mc.Error)
#         return False

# def select_one_bills(bill_id):
#     try:
#         mydb = mc.connect(host=host, user=user, password=password, database=database)
#         cursor = mydb.cursor()
#         cursor.execute("SELECT * FROM delivery where id=".format(bill_id))
#         result = cursor.fetchone()
#         return result
#     except mc.Error as e:
#         print(mc.Error)
#         return e
