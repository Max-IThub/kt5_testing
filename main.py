import sqlite3

def create_table(cursor, table_name, columns):
    query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(columns)}
    );
    '''
    cursor.execute(query)
    print(f"Таблица {table_name} создана")

def main():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Успешно подключено к SQLite")

        # Создание таблицы Dogs
        dogs_columns = ['ID INTEGER PRIMARY KEY', 'Name TEXT', 'Image TEXT', 'Breed TEXT', 'SubBreed TEXT']
        create_table(cursor, 'Dogs', dogs_columns)

        # Создание таблицы Kennels
        kennels_columns = ['ID INTEGER PRIMARY KEY', 'Country TEXT', 'City TEXT']
        create_table(cursor, 'Kennels', kennels_columns)

        # Создание таблицы Buyers
        buyers_columns = ['ID INTEGER PRIMARY KEY', 'FirstName TEXT', 'LastName TEXT', 'PreferredBreeds TEXT']
        create_table(cursor, 'Buyers', buyers_columns)

        sqlite_connection.commit()
        print("Таблицы успешно созданы")

    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

if __name__ == '__main__':
    main()
