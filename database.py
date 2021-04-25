import psycopg2
import datetime


class Database:

    def __init__(self):
        self.username = 'postgres'
        self.password = '07041992'
        self.database = 'Light'
        self.port = 5432 # default

    def add_dict_to_db(self, d):
        # connect to database
        print('Adding values to database...')
        with psycopg2.connect(dbname=self.database, host='localhost', user=self.username, password=self.password,
                              port=self.port) as con:
            cursor = con.cursor()
            try:
                cursor.execute(
                    """INSERT INTO "sensor_data"(s_id, name, value, measurement_unit, date) VALUES (%s,%s,%s,%s,%s)""",
                    (d['s_id'], d['name'], d['value'], d['measurement_unit'], datetime.datetime.now()))
                print(f"Success. {d} added to database.")
            except psycopg2.Error as e:
                print(e)
            # close communication with the database
            cursor.close()
            con.commit()



