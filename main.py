import pymysql
from config import connection


def create_table():
    global connection
    with connection.cursor() as cursor:
        create_table_query = "select * from users"
        cursor.execute(create_table_query)
        print(create_table_query)


def insert_data():
    global connection
    with connection.cursor() as cursor:
        insert_query = ""
        cursor.execute(insert_query)


create_table()


connection.close()
