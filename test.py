import sqlite3
import pytest
import allure


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

def test_insert_dog(database_connection):
    with allure.step("Выполнение INSERT-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Dogs (Name, Breed) VALUES (?, ?)", ("Fido", "Golden Retriever"))
            conn.commit()

        with allure.step("Проверка, что собака была добавлена"):
            check_dog_added(database_connection, "Fido", "Golden Retriever")

def test_select_dog(database_connection):
    with allure.step("Выполнение SELECT-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Breed FROM Dogs WHERE Name = ?", ("Fido",))
            result = cursor.fetchone()
            assert result is not None

def test_update_dog(database_connection):
    with allure.step("Выполнение UPDATE-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Dogs SET Breed = ? WHERE Name = ?", ("Labrador Retriever", "Fido"))
            conn.commit()

        with allure.step("Проверка, что порода собаки была обновлена"):
            with database_connection as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Breed FROM Dogs WHERE Name = ?", ("Fido",))
                result = cursor.fetchone()
                assert result is not None

def test_delete_dog(database_connection):
    with allure.step("Выполнение DELETE-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Dogs WHERE Name = ?", ("Fido",))
            conn.commit()


if __name__ == '__main__':
    pytest.main([__file__])
