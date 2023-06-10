import mysql.connector

class Connection:
    def __init__(self, host, user, password):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE Database IF NOT EXISTS Produtos")