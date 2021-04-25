import sqlite3

class DataBase():
    def __init__(self, filename):
        try:
            sqlite_connection = sqlite3.connect(filename, check_same_thread=False)
            self.cursor = sqlite_connection.cursor()
            print("База данных создана и успешно подключена к SQLite")

            sqlite_select_query = "select sqlite_version();"
            self.cursor.execute(sqlite_select_query)
            record = self.cursor.fetchall()
            print("Версия базы данных SQLite: ", record)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
    
    def addSiteData(self, data):
        try:
            self.cursor.execute(
                f"""INSERT INTO FullSites ('{data['id']}', {data['timestamp']}, '{data['status']}', '{data['url']}', '{data['title']}');"""
            )
            return "OK"
        except sqlite3.Error as error:
            print("Ошибка при создании таблицы: ", error)
            print(error)

    def addURLData(self, data):
        try:
            self.cursor.execute(
                "INSERT INTO SiteLists (ID, URL) VALUES ('" +
                 data['id'] + "', '" + data['url'] + "');"
            )
            print("OK")
        except sqlite3.Error as error:
            print("Ошибка при создании таблицы: ", error)
            return str(error)
            