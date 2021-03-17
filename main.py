from decouple import config
import pandas as pd
import pymssql
import utility
import os


# Pobranie zmiennych srodowiskowych
server = config('SERVER')
user = config('DB_USER')
password = config('DB_PASSWORD')
database = config('DATABASE')

try:
    conn = pymssql.connect(server, user, password, database)
except pymssql.OperationalError as err:
    print('Error!', err)
    exit(1)

# utility.print_products(conn)
sql_query = pd.read_sql_query('''
                                SELECT tw_Id, tw_Symbol, tw_Nazwa, tw_Opis, tc_CenaNetto7 FROM dbo.tw__Towar INNER JOIN dbo.tw_Cena ON tw_Id = tc_IdTowar WHERE tw_Zablokowany = 0
                              '''
                              , conn)

df = pd.DataFrame(sql_query)
# Zamkniecie polaczenia
conn.close()
df.to_csv(os.path.join(os.getcwd(), 'csv', 'produkty.csv'), index=False)