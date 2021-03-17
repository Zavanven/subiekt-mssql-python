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
    '''Funkcja drukujaca wybrane kolumny
    
    Do zmiany.'''

    cursor = conn.cursor()
    cursor.execute("SELECT tw_Id, tw_Symbol, tw_Nazwa, tw_Opis, tc_CenaNetto7 FROM dbo.tw__Towar INNER JOIN dbo.tw_Cena ON tw_Id = tc_IdTowar WHERE tw_Zablokowany = 0") 
    row = cursor.fetchone() 
    while row: 
        print(row)
        row = cursor.fetchone()