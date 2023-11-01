import ntplib
import time

def get_time_difference():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('192.168.1.78', port=5050)

    server_time = response.tx_time  # Get the server time
    client_time = time.time()  # Get the client's current time

    time_diff = server_time - client_time  # Calculate time difference

    return time_diff

# Get the time difference
time_difference = get_time_difference()

# Store the time difference in a file
with open('time_difference.txt', 'w') as file:
    file.write(f"The time difference between server and client is {time_difference} seconds.")

print("Time difference saved to 'time_difference.txt' file.")
