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

HEADER = 64
PORT = 5050
SERVER = '192.168.1.78'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    # client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

start_time = time.time()  # Record the start time
duration = 5 * 60  # 5 minutes in seconds

while time.time() - start_time <= duration:
    send("Hello world"+str(time.time() - start_time))
    time.sleep(0.5)
send(DISCONNECT_MESSAGE)
print("five minutes done.")