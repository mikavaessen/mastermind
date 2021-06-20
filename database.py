import pyodbc

# Class that handles connection to the database
class Database():
    def __init__(self):
        # Connect to the database with the connectionstring
        self.conStr = 'Driver={SQL Server};\nServer=LAPTOP-9519V91I\MSSQLSERVER01;\nDatabase=Mastermind;\nTrusted_Connection=yes;'
        #self.conStr = 'Driver={SQL Server};\nServer=DESKTOP-3V6BQPT;\nDatabase=Mastermind;\nTrusted_Connection=yes;'
        self.conn = pyodbc.connect(self.conStr)

    def getNames(self):
        # Get all player names in a list
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM data")
        data = list()
        for row in cursor:
            data.append(row[0])
        return data

    def getPlayerData(self, name:str):
        # Get data of all games for a specific player
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM data WHERE Name = '{name}' ORDER BY Game DESC")
        retVal = []
        for row in cursor:
            retVal.append(row)
        return retVal

    def addGame(self, name:str, tries:int, result:str, difficulty:str):
        # Add a game to the database
        if self.checkForbidden(name):
            return
        cursor = self.conn.cursor()
        cursor.execute(f"EXEC addGame '{name}', {tries}, '{result}', '{difficulty}'")
        self.conn.commit()

    def checkForbidden(self, string):
        # Check for potential SQL injection
        forbiiden = "';," + '"'
        for i in string:
            for j in forbiiden:
                if i == j:
                    return True
        return False

    def close(self):
        del self.conn