import pymysql

connection = pymysql.connect(
        host='217.107.219.186',
        port=3306,
        user='038147009_pract',
        password='K9myj3;_p2uz',
        database='darkelza_galiullin_db',
        cursorclass=pymysql.cursors.DictCursor
    )

token = '7250507637:AAHhLqUtN0EZWz9Nd0ojpywHrfZ5FrRWW6A'
