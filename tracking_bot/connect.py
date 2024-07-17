import pymysql
import config
import datetime
from datetime import time
connect = config.connection


def add_new_user(id, name, date_reg, day_start, day_end):
    global connect
    with connect.cursor() as cursor:
        sql_request = "INSERT INTO `users` (`tg_id`, `name`, `date_reg`, `day_start`,`day_end`) \
                                VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql_request, (id, name, date_reg, day_start, day_end))
        connect.commit()


# пример добавления юзера add_new_user(123123, 'имя', '2022-08-08', '8:00', '22:00')


def select_start_and_end_day(tg_id):
    global connect
    with connect.cursor() as cursor:
        sql_request = "select `day_start`, `day_end` from `users` where `tg_id` = %s"
        cursor.execute(sql_request, (tg_id))
        result = cursor.fetchone()
        return [result['day_start'], result['day_end']]
# [datetime.timedelta(seconds=1222), datetime.timedelta(seconds=28800)]




def change_start_or_end_day(tg_id, start_or_end, time):
    global connect
    with connect.cursor() as cursor:
        sql_request = f"UPDATE `users` SET `{start_or_end}` = %s WHERE `tg_id` = %s;"
        cursor.execute(sql_request, (time, tg_id))
        connect.commit()

# change_start_or_end_day(123123, 'day_start', '11:00:00')

def codes_for_id(tg_id):
    global connect
    with connect.cursor() as cursor:
        sql_request = ("select `code`, `value_code` from `codes` \
                       where user_id =(select id from users where tg_id = %s)")
        cursor.execute(sql_request, tg_id)
        result = cursor.fetchall()
        return result


def add_new_code(tg_id, code, value_code):
    global connect
    with connect.cursor() as cursor:
        sql_request = "INSERT INTO `codes` (`user_id`, `code`, `value_code`) \
                                VALUES ((select `id` from `users` where `tg_id` = %s), %s, %s);"
        cursor.execute(sql_request, (tg_id, code, value_code))
        connect.commit()
#add_new_code(123123, 12, "завтрак")


def delete_code(tg_id, code):
    global connect
    with connect.cursor() as cursor:
        sql_request = "DELETE FROM `codes` WHERE `user_id` = (select `id` from `users` where `tg_id` = %s) and `code` = %s"
        cursor.execute(sql_request, (tg_id, code))
        connect.commit()
#delete_code(123123, 12)


def delete_all_codes(tg_id):
    global connect
    with connect.cursor() as cursor:
        sql_request = "DELETE FROM `codes` WHERE `user_id` = (select `id` from `users` where `tg_id` = %s)"
        cursor.execute(sql_request, tg_id)
        connect.commit()


async def fetch_and_send_data(chat_id):
    global connect
    with connect.cursor() as cursor:
        sql_request = "SELECT value_code FROM `codes` WHERE `user_id` = (select `id` from `users` where `tg_id` = %s)"
        cursor.execute(sql_request, chat_id)
        connect.commit()


