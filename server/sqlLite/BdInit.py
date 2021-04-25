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
            print(data['id'])
            print(str(data['settings']['timestamp']))
            print(data['settings']['status'])
            print(data['url'])
            print(data['title'])
            print(str(data['settings']['timeOut']))
            print("INSERT INTO FullSites (ID, TimeStamp, Status, URL, Title, Timeout) VALUES ('" + data['id'] + "', " + str(data['settings']['timestamp']) + ", '" + data['settings']['status'] + "', '" + data['url'] + "', '" + data['title'] + "', " + str(data['settings']['timeOut']) + ");")
            self.cursor.execute("INSERT INTO FullSites (ID, TimeStamp, Status, URL, Title, Timeout) VALUES ('" + data['id'] + "', " + str(data['settings']['timestamp']) + ", '" + data['settings']['status'] + "', '", data['url'] + "', '" + data['title'] + "', " + str(data['settings']['timeOut']) + ");")
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
            