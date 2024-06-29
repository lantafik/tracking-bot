import boto3
import datetime
import config
from decimal import Decimal

arr = [[datetime.time(5, 0), datetime.time(5, 15)], [datetime.time(5, 15), datetime.time(5, 30)],
       [datetime.time(5, 30), datetime.time(5, 45)], [datetime.time(5, 45), datetime.time(6, 0)],
       [datetime.time(6, 0), datetime.time(6, 15)], [datetime.time(6, 15), datetime.time(6, 30)],
       [datetime.time(6, 30), datetime.time(6, 45)], [datetime.time(6, 45), datetime.time(7, 0)],
       [datetime.time(7, 0), datetime.time(7, 15)], [datetime.time(7, 15), datetime.time(7, 30)],
       [datetime.time(7, 30), datetime.time(7, 45)], [datetime.time(7, 45), datetime.time(8, 0)],
       [datetime.time(8, 0), datetime.time(8, 15)], [datetime.time(8, 15), datetime.time(8, 30)],
       [datetime.time(8, 30), datetime.time(8, 45)], [datetime.time(8, 45), datetime.time(9, 0)],
       [datetime.time(9, 0), datetime.time(9, 15)], [datetime.time(9, 15), datetime.time(9, 30)],
       [datetime.time(9, 30), datetime.time(9, 45)], [datetime.time(9, 45), datetime.time(10, 0)],
       [datetime.time(10, 0), datetime.time(10, 15)], [datetime.time(10, 15), datetime.time(10, 30)],
       [datetime.time(10, 30), datetime.time(10, 45)], [datetime.time(10, 45), datetime.time(11, 0)],
       [datetime.time(11, 0), datetime.time(11, 15)], [datetime.time(11, 15), datetime.time(11, 30)],
       [datetime.time(11, 30), datetime.time(11, 45)], [datetime.time(11, 45), datetime.time(12, 0)],
       [datetime.time(12, 0), datetime.time(12, 15)], [datetime.time(12, 15), datetime.time(12, 30)],
       [datetime.time(12, 30), datetime.time(12, 45)], [datetime.time(12, 45), datetime.time(13, 0)],
       [datetime.time(13, 0), datetime.time(13, 15)], [datetime.time(13, 15), datetime.time(13, 30)],
       [datetime.time(13, 30), datetime.time(13, 45)], [datetime.time(13, 45), datetime.time(14, 0)],
       [datetime.time(14, 0), datetime.time(14, 15)], [datetime.time(14, 15), datetime.time(14, 30)],
       [datetime.time(14, 30), datetime.time(14, 45)], [datetime.time(14, 45), datetime.time(15, 0)],
       [datetime.time(15, 0), datetime.time(15, 15)], [datetime.time(15, 15), datetime.time(15, 30)],
       [datetime.time(15, 30), datetime.time(15, 45)], [datetime.time(15, 45), datetime.time(16, 0)],
       [datetime.time(16, 0), datetime.time(16, 15)], [datetime.time(16, 15), datetime.time(16, 30)],
       [datetime.time(16, 30), datetime.time(16, 45)], [datetime.time(16, 45), datetime.time(17, 0)],
       [datetime.time(17, 0), datetime.time(17, 15)], [datetime.time(17, 15), datetime.time(17, 30)],
       [datetime.time(17, 30), datetime.time(17, 45)], [datetime.time(17, 45), datetime.time(18, 0)],
       [datetime.time(18, 0), datetime.time(18, 15)], [datetime.time(18, 15), datetime.time(18, 30)],
       [datetime.time(18, 30), datetime.time(18, 45)], [datetime.time(18, 45), datetime.time(19, 0)],
       [datetime.time(19, 0), datetime.time(19, 15)], [datetime.time(19, 15), datetime.time(19, 30)],
       [datetime.time(19, 30), datetime.time(19, 45)], [datetime.time(19, 45), datetime.time(20, 0)],
       [datetime.time(20, 0), datetime.time(20, 15)], [datetime.time(20, 15), datetime.time(20, 30)],
       [datetime.time(20, 30), datetime.time(20, 45)], [datetime.time(20, 45), datetime.time(21, 0)],
       [datetime.time(21, 0), datetime.time(21, 15)], [datetime.time(21, 15), datetime.time(21, 30)],
       [datetime.time(21, 30), datetime.time(21, 45)], [datetime.time(21, 45), datetime.time(22, 0)],
       [datetime.time(22, 0), datetime.time(22, 15)], [datetime.time(22, 15), datetime.time(22, 30)],
       [datetime.time(22, 30), datetime.time(22, 45)], [datetime.time(22, 45), datetime.time(23, 0)],
       [datetime.time(23, 0), datetime.time(23, 15)], [datetime.time(23, 15), datetime.time(23, 30)],
       [datetime.time(23, 30), datetime.time(23, 45)], [datetime.time(23, 45), datetime.time(0, 0)],
       [datetime.time(0, 0), datetime.time(0, 15)], [datetime.time(0, 15), datetime.time(0, 30)],
       [datetime.time(0, 30), datetime.time(0, 45)], [datetime.time(0, 45), datetime.time(1, 0)],
       [datetime.time(1, 0), datetime.time(1, 15)], [datetime.time(1, 15), datetime.time(1, 30)],
       [datetime.time(1, 30), datetime.time(1, 45)], [datetime.time(1, 45), datetime.time(2, 0)],
       [datetime.time(2, 0), datetime.time(2, 15)], [datetime.time(2, 15), datetime.time(2, 30)],
       [datetime.time(2, 30), datetime.time(2, 45)], [datetime.time(2, 45), datetime.time(3, 0)],
       [datetime.time(3, 0), datetime.time(3, 15)], [datetime.time(3, 15), datetime.time(3, 30)],
       [datetime.time(3, 30), datetime.time(3, 45)], [datetime.time(3, 45), datetime.time(4, 0)],
       [datetime.time(4, 0), datetime.time(4, 15)], [datetime.time(4, 15), datetime.time(4, 30)],
       [datetime.time(4, 30), datetime.time(4, 45)]]

# Connection database
database = boto3.resource(
    'dynamodb',
    endpoint_url=config.USER_STORAGE_URL,
    region_name='ru-central1',
    aws_access_key_id=config.AWS_PUBLIC_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY
)


def update_pivot(id_int, id_num, flag):
    global database
    forecast = database.Table('PIVOT_TABLE')
    forecast.put_item(
        Item={
            'ID_INT': id_int,
            'ID_NUM': id_num,
            'FLAG': flag
        }
    )


def put_table_numbers(date, number, time, table):
    global database
    global arr
    forecast = database.Table(table)
    forecast.put_item(
        Item={
            'ID': config.id,
            'NUMBER': number,
            'DATE': f'{date}',
            'TIME': f'{time}'
        }
    )
    config.change_id()


def update_table_numbers(number, date, time, table):
    global database
    global arr
    forecast = database.Table(table)
    forecast.update_item(
        Key={
            'DATE': date,
            'TIME': time
        },
        UpdateExpression='set #d = :d',
        ExpressionAttributeNames={
            '#d': 'NUMBER'
        },
        ExpressionAttributeValues={
            ':d': f'{number}'
        }
    )


def get_id_number(date, time, table):
    global database, arr
    forecast = database.Table(table)
    response = forecast.get_item(
        Key={
            'DATE': date,
            'TIME': time
        },
        ProjectionExpression='ID'
    )
    item = response.get('Item')
    item = response.get('Item')['ID']
    return item


def get_id_interval(left_interval, right_interval):
    global database
    global arr
    forecast = database.Table('Intervals')
    response = forecast.get_item(
        Key={
            'LEFT_INTERVAL': left_interval,
            'RIGHT_INTERVAL': right_interval
        },
        ProjectionExpression='ID_INT'
    )
    item = response.get('Item')['ID_INT']
    return item


def interval():
    global database
    global arr
    forecast = database.Table("Intervals")
    k = 0
    for i in arr:
        k += 1
        forecast.put_item(
            Item={
                'ID_INT': Decimal(k),
                'LEFT_INTERVAL': i[0].strftime('%H:%M'),
                'RIGHT_INTERVAL': i[1].strftime('%H:%M'),
                'PLAN_CHECKER': '0',
                'FACT_CHECKER': '0'
            }
        )


def checking(left_interval, right_interval, type_checker):
    global database
    forecast = database.Table('Intervals')
    response = forecast.get_item(
        Key={
            'LEFT_INTERVAL': left_interval,
            'RIGHT_INTERVAL': right_interval
        },
        ProjectionExpression=type_checker
    )
    item = response.get('Item')[type_checker]
    return item


def cycle_update_checker():
    global database
    global arr
    forecast = database.Table('Intervals')
    for i in arr:
        left_interval, right_interval = i[0].strftime('%H:%M'), i[1].strftime('%H:%M')
        forecast.update_item(
            Key={
                'LEFT_INTERVAL': left_interval,
                'RIGHT_INTERVAL': right_interval
            },
            UpdateExpression='set #d = :d, #s = :s',
            ExpressionAttributeNames={
                '#d': 'PLAN_CHECKER',
                '#s': 'FACT_CHECKER'
            },
            ExpressionAttributeValues={
                ':d': '0',
                ':s': '0'
            }
        )


def update_checking(left_interval, right_interval, time, type_checker):
    global database
    forecast = database.Table('Intervals')
    forecast.update_item(
        Key={
            'LEFT_INTERVAL': left_interval,
            'RIGHT_INTERVAL': right_interval
        },
        UpdateExpression='set #d = :d',
        ExpressionAttributeNames={
            '#d': type_checker
        },
        ExpressionAttributeValues={
            ':d': time
        }
    )
