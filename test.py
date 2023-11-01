import os
import time

FORMAT = 'utf-8'
t = time.time()
euler = 271828
pi = 31415926
datetimedec = int(t)
microsec = int((t - int(t))*1000000)
message = euler.to_bytes(4, 'big') + pi.to_bytes(4, 'big') + datetimedec.to_bytes(4, 'big') + microsec.to_bytes(4, 'big')
# message = msg.encode(FORMAT)
msg_length = len(message)
message += os.urandom(250 - msg_length)

# message = message.decode(FORMAT)
ts = int(int(message.hex()[16:24], 16)) + float("0." + str(int(message.hex()[24:32], 16)))

print(ts)
# print(len(message))