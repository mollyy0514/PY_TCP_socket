# import socket

# s = socket.socket()

# host = "0.0.0.0"
# port = 12345

# # connect to the server on local computer
# s.connect((host, port))

# # receive data from the server and decoding to get the string.
# print (s.recv(1024).decode())

# while True:
#     for i in range(10):
#         s.send(str(i).encode())
#         data = s.recv(1024)
#         print(f"server send: {data}")

# # close the connection
# s.close() 

import socket
import time
import os

HEADER = 64
PORT = 5050
SERVER = '192.168.1.78'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

start_time = time.time()  # Record the start time
duration = 1 * 60  # 5 minutes in seconds

packet_length = 250
euler = 271828
pi = 31415926
while time.time() - start_time <= duration:
    t = time.time()
    datetimedec = int(t)
    microsec = int((t - int(t))*1000000)

    redundant = os.urandom(packet_length-4*4)
    outdata = euler.to_bytes(4, 'big') + pi.to_bytes(4, 'big') + datetimedec.to_bytes(4, 'big') + microsec.to_bytes(4, 'big') + redundant
    client.send(outdata)
    time.sleep(0.5)

client.send(DISCONNECT_MESSAGE)
print("five minutes done.")