import mysql.connector
from mysql.connector import Error


def connect_open():
    try:
        conn = mysql.connector.connect(host="localhost", user="DiDiana", password="Rhenjqhfphf520", database="shopTeleBot")
        if conn.is_connected():
            cur = conn.cursor()
            print('Connected to MySQL database')
            my_tuple = (conn, cur)
            return my_tuple
    except Error as err:
        print("Something wrong", err)


def connect_close():
    c_tuple = connect_open()
    try:
        if connect_open():
            c_tuple[1].close()
            c_tuple[0].close()
    except Error as err:
        print("Smth wrong", err)


def find_users(chat_id):
    c_tuple = connect_open()
    sql = "SELECT chatId FROM Users"
    try:
        c_tuple[1].execute(sql)
        for x in c_tuple[1]:
            if x == (chat_id,):
                return True
        return False
    except Error as err:
        print("Error occurred: ", err)
    finally:
        connect_close()


def add_user(message):
    c_tuple = connect_open()
    sql = "INSERT INTO Users(chatId, user_name, user_firstName, user_lastName, user_status) " \
          "VALUES ('%(chId)s', '%(us_name)s', '%(us_firstName)s', '%(us_lastName)s', '%(us_stat)s')" \
          % {"chId": message.chat.id, "us_name": message.from_user.username,
             "us_firstName": message.from_user.first_name, "us_lastName": message.from_user.last_name, "us_stat": "user"}
    try:
        c_tuple[1].execute(sql)
        c_tuple[0].commit()
    except Error as err:
        print("Failed to insert into MySQL table {}".format(err))
    finally:
        print("Все нормально.")
        connect_close()


def find_products(cat_name):
    c_tuple = connect_open()
    sql = "SELECT prod_name FROM Products WHERE categories_id IN (SELECT id from Categories " \
          "WHERE cat_name = '%s' )" % cat_name
    try:
        c_tuple[1].execute(sql)
        prod_list = []
        test = c_tuple[1].fetchall()
        for x in test:
            x = list(x)
            prod_list.append(x)
        return prod_list
    except Error as err:
        print("Error occurred: ", err)
    finally:
        connect_close()


def find_categories():
    c_tuple = connect_open()
    sql = "SELECT cat_name FROM Categories"
    try:
        c_tuple[1].execute(sql)
        cat_list = []
        for x in c_tuple[1]:
            x = list(x)
            cat_list.append(x)
        return cat_list
    except Error as err:
        print("Error occurred: ", err)
    finally:
        connect_close()


# на будущее
# myDb = mysql.connector.connect(host="localhost", user="DiDiana", password="Rhenjqhfphf520", database="shopTeleBot")
# print(myDb)
# myCursor = myDb.cursor()
#
#
# def show_table():
#     myCursor.execute("SHOW TABLES;")
#     for x in myCursor:
#         print(x)
#
#
# def show_users_db():
#     myCursor.execute("SELECT * FROM Users;")
#     for x in myCursor:
#         # print(x)
#         return x
#
#
# def show_products_db():
#     myCursor.execute("SELECT * FROM Products;")
#     for x in myCursor:
#         print(x)
#
#
# def show_images_db():
#     myCursor.execute("SELECT * FROM Images;")
#     for x in myCursor:
#         print(x)
#
#
# def show_categories_db():
#     myCursor.execute("SELECT * FROM Categories;")
#     for x in myCursor:
#         print(x)
#
#
# def show_orders_db():
#     myCursor.execute("SELECT * FROM Orders;")
#     for x in myCursor:
#         print(x)


