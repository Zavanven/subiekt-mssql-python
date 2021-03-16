from os import getenv
import pymssql

# Pobranie zmiennych srodowiskowych
server = getenv('SERVER')
user = getenv('USER')
password = getenv('PASSWORD')
database = genenv('DATABASE')

try:
    conn = pymssql.connect(server, user, password, database)
except pymssql.OperationalError as err:
    print('Error!', err)