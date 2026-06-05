import socket
import json

from logger import initialize_csv
from logger import log_packet

HOST = "127.0.0.1"
PORT = 9999

initialize_csv()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("EyeNet Receiver Started")
print(f"Listening on {HOST}:{PORT}")

while True:

    data, addr = server.recvfrom(1024)

    packet = json.loads(data.decode())

    log_packet(packet)

    print("\nReceived Packet")
    print(packet)