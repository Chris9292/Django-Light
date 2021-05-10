import socket
from api.database import Database
from datetime import datetime
import psycopg2
import msvcrt


def add_record_to_db(data, cursor):
    print('Adding record to database...')
    try:
        cursor.execute("""INSERT INTO "sensor_data" (s_id, name, value, date) VALUES (%s,%s,%s,%s)""", (data['s_id'], data['name'], data['value'], datetime.now()))
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return
    cursor.commit()
    print(f"Success. {data} added to database.")


UDP_IP = socket.gethostname() # returns the IP of this device
UDP_PORT = 5005  # port number
print(UDP_IP)
# initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to address
sock.bind(('192.168.1.4', UDP_PORT))

print("waiting for incoming messages...")
print("press CTRL+C to exit")

db = Database()
con, cursor = db.connect()

while True:
    message, addr = sock.recvfrom(12)  # receive data with certain buffer size
    print(f"received following message: {message} from {addr}")  # decode incoming message

    data = message.decode('utf-8')     # dict format
    add_record_to_db(data, cursor)

    if msvcrt.kbhit():
        print("Key interruption. Program closing...")
        break

con.close()
cursor.close()
