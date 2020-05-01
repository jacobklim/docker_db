import os
import pandas as pd
import sqlalchemy as db

WORK_DIR = os.path.dirname(__file__)

config = {
    'host': 'mysql',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'sales'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = db.create_engine(connection_str)

connection = engine.connect()

df = pd.read_excel(os.path.join(WORK_DIR, 'data/data.xlsx'))
df.to_sql('sales_table', connection, if_exists='replace')