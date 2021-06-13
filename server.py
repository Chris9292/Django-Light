import socket
from api.database import Database
import psycopg2
import msvcrt
import pickle
import time


UDP_IP = socket.gethostname() # returns the IP of this device
UDP_PORT = 5015  # port number
print(UDP_IP)
# initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
# bind socket to address
sock.bind((socket.gethostname(), UDP_PORT))

print("waiting for incoming messages...")
print("press CTRL+C to exit")

db = Database()
con, cursor = db.connect()

START_TIME = time.time()
while True:
    data, addr = sock.recvfrom(136)  # receive data with certain buffer size
    data = pickle.loads(data)

    print(f"received following data: {data} from {addr}\n")  # decode incoming message

    print('Adding record to database...')
    try:
        cursor.execute("""INSERT INTO "sensor_data" (name, value, date) VALUES (%s,%s,%s)""",
                       (data["name"], data["value"], data["date"]))
    except psycopg2.Error as e:
        print(f"Error: {e}")
        continue
    con.commit()
    print(f"Success. {data} added to database.\n")


    if msvcrt.kbhit():
        print("Key interruption. Program closing...")
        break

    # if (time.time() - START_TIME) > 60 :
    #     START_TIME = time.time()
    #     print("1 minute passed since server is on.")
    #     cursor.execute("""DELETE FROM sensor_data""")
    #     con.commit()

con.close()
cursor.close()
