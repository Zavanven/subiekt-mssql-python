def check_version(conn):
    '''Funkcja wyswietlajaca wersje bazy danych
    
    Glownie uzywana do sprawdzania polaczenia z baza danych.'''

    cursor = conn.cursor()
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()

def print_products(conn):
    '''Funkcja drukujaca 5 pierwszych kolumn z listy towarow.
    
    Do zmiany.'''

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.tw__Towar WHERE tw_Zablokowany=0") 
    row = cursor.fetchone() 
    while row: 
        print(row[0], row[1], row[2], row[3], row[4])
        row = cursor.fetchone()