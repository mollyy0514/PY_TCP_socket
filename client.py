import socket
import time
import os
import subprocess
from datetime import date

HEADER = 64
PORT = 5050
# SERVER = '140.112.20.183'
SERVER = '192.168.1.78'
# SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = b"!DISCONNECT"

def start_tcpdump():
    today = date.today()
    today = today.strftime("%Y%m%d")
    filepath = f'./data/capturetcp_c_{today}.pcap'
    command = f'echo molly900514 | sudo -S tcpdump port {PORT} -w {filepath}'
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    return p

def close_tcpdump(p):
    p.send_signal(subprocess.signal.SIGTERM)

p = start_tcpdump()
# time.sleep(10)

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

close_tcpdump(p)