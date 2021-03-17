from decouple import config
import pymssql
import utility

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

utility.check_version(conn)

# # Print listy wszystkich produktow
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM dbo.tw__Towar WHERE tw_Zablokowany=0") 
# row = cursor.fetchone() 
# while row: 
#     print(row[0], row[1], row[2], row[3], row[4])
#     row = cursor.fetchone()


conn.close()