import sqlite3
import pytest

@pytest.fixture(scope='session')
def database_connection():
    connection = sqlite3.connect('sqlite_python.db')
    yield connection
    connection.close()

def check_dog_added(database_connection, name, breed):
    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Breed FROM Dogs WHERE Name = ? AND Breed = ?", (name, breed))
        result = cursor.fetchone()
        assert result is not None

def test_insert_dogs(database_connection):
    # Добавление собак
    dogs_to_insert = [("Buddy", "Labrador Retriever"),
                      ("Max", "German Shepherd"),
                      ("Lucy", "Golden Retriever")]

    with database_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO Dogs (Name, Breed) VALUES (?, ?)", dogs_to_insert)
        conn.commit()

    for dog_name, dog_breed in dogs_to_insert:
        check_dog_added(database_connection, dog_name, dog_breed)

def test_select_dogs(database_connection):
    # Выборка информации о собаках
    dogs_to_select = ["Buddy", "Max", "Lucy"]

    with database_connection as conn:
        cursor = conn.cursor()
        for dog_name in dogs_to_select:
            cursor.execute("SELECT Name, Breed FROM Dogs WHERE Name = ?", (dog_name,))
            result = cursor.fetchone()
            assert result is not None

def test_update_dog_breed(database_connection):
    # Обновление породы собаки
    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Dogs SET Breed = ? WHERE Name = ?", ("Labrador Mix", "Buddy"))
        conn.commit()

    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Breed FROM Dogs WHERE Name = ?", ("Buddy",))
        result = cursor.fetchone()
        assert result is not None

def test_delete_dogs(database_connection):
    # Удаление собак
    dogs_to_delete = ["Buddy", "Max", "Lucy"]

    with database_connection as conn:
        cursor = conn.cursor()
        for dog_name in dogs_to_delete:
            cursor.execute("DELETE FROM Dogs WHERE Name = ?", (dog_name,))
            conn.commit()

    for dog_name in dogs_to_delete:
        with pytest.raises(AssertionError):
            check_dog_added(database_connection, dog_name, "Labrador Mix")

if __name__ == '__main__':
    pytest.main([__file__])
