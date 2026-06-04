import socket
import json

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("EyeNet Receiver Started")
print(f"Listening on {HOST}:{PORT}")

while True:

    data, addr = server.recvfrom(1024)

    packet = json.loads(data.decode())

    print("\nReceived Packet")
    print(packet)