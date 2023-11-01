import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname()
SERVER = '0.0.0.0'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # will be pass until there's a message accepted from client
        # msg_length = conn.recv(HEADER).decode(FORMAT)
        # if msg_length:  # checking if msg is not none
        # msg_length = int(msg_length)
        # msg = conn.recv(1024).decode(FORMAT)
        msg = conn.recv(1024)
        if msg != DISCONNECT_MESSAGE:
            # seq = int(msg.hex()[32:40], 16)
            ts = int(int(msg.hex()[16:24], 16)) + float("0." + str(int(msg.hex()[24:32], 16)))
        else:
            connected = False
        print(f"[{addr}] {ts}")
        # conn.send("Msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # when a new connection occurs, we're going to pass that connection to hadle_client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # print how many threads is active on this process, which reoresent the amount of clients connected, 
        # there's a thread always running to listen
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()