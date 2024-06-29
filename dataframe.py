import datetime

import config, boto3, pandas as pd

database = boto3.resource(
    'dynamodb',
    endpoint_url=config.USER_STORAGE_URL,
    region_name='ru-central1',
    aws_access_key_id=config.AWS_PUBLIC_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY
)

df_intervals = pd.DataFrame((database.Table('Intervals')).scan()['Items'])[
    ['ID_INT', 'LEFT_INTERVAL', 'RIGHT_INTERVAL']].sort_values(by='ID_INT')

today = datetime.date.today()
day_of_week = today.weekday()
monday = today - datetime.timedelta(days=day_of_week)
sunday = monday + datetime.timedelta(days=6)
sheet_name = f'{monday} - {sunday}'


def data_frame(date):
    global database, df_intervals
    fact_items = pd.DataFrame(database.Table('FACT_Numbers').scan()['Items'])
    plan_items = pd.DataFrame(database.Table('PLAN_Numbers').scan()['Items'])
    pivot_items = pd.DataFrame(database.Table('PIVOT_TABLE').scan()['Items'])
    df_fact_numb = (fact_items[['ID', 'NUMBER']]
        .rename(columns={'ID': 'FACT', 'NUMBER': 'FACT_NUMBER'})
        .loc[pd.to_datetime(fact_items['DATE']) == date])
    df_plan_numb = (plan_items[['ID', 'NUMBER']]
        .rename(columns={'ID': 'PLAN', 'NUMBER': 'PLAN_NUMBER'})
        .loc[pd.to_datetime(plan_items['DATE']) == date])
    df_plan_pivot = (pivot_items[pivot_items['FLAG'] == 'PLAN'])[['ID_INT', 'ID_NUM']]
    df_fact_pivot = (pivot_items[pivot_items['FLAG'] == 'FACT'])[['ID_INT', 'ID_NUM']]
    result_df = pd.merge(df_intervals, df_plan_pivot.rename(columns={'ID_NUM': 'PLAN'}), on='ID_INT', how='left')
    result_df = result_df.merge(df_fact_pivot.rename(columns={'ID_NUM': 'FACT'}), on='ID_INT', how='left')
    result_df[['PLAN', 'FACT']] = result_df[['PLAN', 'FACT']].astype(float)
    result_df = result_df.merge(df_plan_numb, on='PLAN', how='left').merge(df_fact_numb, on='FACT', how='left')
    return result_df


def change_column(plan_or_fact, result_df):
    list_numb = result_df[plan_or_fact].tolist()
    processing_variable = ''
    for i in range(len(list_numb)):
        if type(list_numb[i]) == str:
            processing_variable = list_numb[i]
        if processing_variable != '':
            list_numb[i] = processing_variable
    result_df[plan_or_fact] = list_numb


def columns_of_date(date):
    result_df = data_frame(date)
    change_column('PLAN_NUMBER', result_df)
    change_column('FACT_NUMBER', result_df)
    result_df = result_df[['PLAN_NUMBER', 'FACT_NUMBER']]
    date = date.strftime('%Y-%m-%d')
    result_df = result_df.rename(columns={'PLAN_NUMBER': f'PLAN_{date}', 'FACT_NUMBER': f'FACT_{date}'})
    return result_df


def add_date_columns(df, sheet_name):
    file = pd.read_excel('C:\\Users\\Lantafik\\PycharmProjects\\pythonProject1\\aio_project\\output.xlsx')
    file = file.join(df)
    file.to_excel(r'output.xlsx', sheet_name=sheet_name)


def new_sheet(sheet_name):
    global df_intervals
    writer = pd.ExcelWriter(r'output.xlsx', engine='xlsxwriter')
    df_intervals.to_excel(writer, sheet_name=sheet_name, index=False)
    writer._save()




