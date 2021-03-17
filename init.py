from decouple import config
import pymssql

# Pobranie zmiennych srodowiskowych
server = config('SERVER')
user = config('DB_USER')
password = config('DB_PASSWORD')
database = config('DATABASE')

try:
    conn = pymssql.connect(server, user, password, database)
except pymssql.OperationalError as err:
    print('Error!', err)