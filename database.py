import pyodbc
from datetime import datetime

class Database():
    def __init__(self):
        self.conStr = 'Driver={SQL Server};\nServer=DESKTOP-3V6BQPT\MSSQLSERVER01;\nDatabase=Mastermind;\nTrusted_Connection=yes;'
        self.conn = pyodbc.connect(self.conStr)

    def getNames(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM data")
        data = list(str)
        for row in cursor:
            data.append(row[0])
        return data

    def getPlayerData(self, name:str):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM data WHERE name = {name}")
        return cursor

    def addGame(self, name:str, tries:int):
        if self.checkForbidden(name):
            return
        cursor = self.conn.cursor()
        now = datetime.now().strftime("%c")
        cursor.execute(f"INSERT INTO data VALUES (NEWID(), {name}, {now}, {tries})")
        self.conn.commit()

    def checkForbidden(self, string):
        forbiiden = "';," + '"'
        for i in string:
            for j in forbiiden:
                if i == j:
                    return True
        return False

    def close(self):
        del self.conn