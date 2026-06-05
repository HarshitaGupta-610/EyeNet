import socket
import json
import random
import time

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("EyeNet Sender Started")

while True:

    radar_packet = {
        "target_id": random.randint(1, 100),
        "range": random.randint(100, 500),
        "velocity": random.randint(200, 900),
        "signal_strength": round(random.uniform(70, 100), 2),
        "packet_size": random.randint(128, 1024),
        "timestamp": time.time()
    }

    client.sendto(
        json.dumps(radar_packet).encode(),
        (HOST, PORT)
    )

    print("Sent:", radar_packet)

    time.sleep(1)