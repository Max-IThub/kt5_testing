import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("БД подключена к SQLite")


    create_dogs_table_query = '''
    CREATE TABLE IF NOT EXISTS Dogs (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Image TEXT,
        Breed TEXT,
        SubBreed TEXT
    );
    '''
    cursor.execute(create_dogs_table_query)
    print("Таблица собак создана")


    create_kennels_table_query = '''
    CREATE TABLE IF NOT EXISTS Kennels (
        ID INTEGER PRIMARY KEY,
        Country TEXT,
        City TEXT
    );
    '''
    cursor.execute(create_kennels_table_query)
    print("Таблица питомников создана")


    create_buyers_table_query = '''
    CREATE TABLE IF NOT EXISTS Buyers (
        ID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        PreferredBreeds TEXT
    );
    '''
    cursor.execute(create_buyers_table_query)
    print("Таблица потенциальныx покупателей создана")

    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к SQLite:", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
