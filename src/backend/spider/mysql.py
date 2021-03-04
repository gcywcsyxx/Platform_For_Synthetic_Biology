import pymysql

class DataBase:
    def __init__ (self, host:str, username:str, password:str, database:str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connect():
        connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            cursorclass = pymysql.cursors.DictCursor
        )
        self.connection = connection
