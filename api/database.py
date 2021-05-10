import psycopg2


class Database:

    def __init__(self):
        self.username = 'postgres'
        self.password = '07041992'
        self.database = 'Light'
        self.host = 'localhost'
        self.port = 5432    # default

    def connect(self):
        # connect to db: return connection + cursor
        con = psycopg2.connect(dbname=self.database, host=self.host, port=self.port, user=self.username, password=self.password)
        return con, con.cursor()
