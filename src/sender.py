import socket
import json
import random
import time

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("EyeNet Sender Started")

while True:

    p = random.random()

    # NORMAL
    if p < 0.70:

        radar_packet = {
            "target_id": random.randint(1, 100),
            "range": random.randint(100, 500),
            "velocity": random.randint(200, 1200),
            "signal_strength": round(random.uniform(50, 100), 2),
            "packet_size": random.randint(128, 2000),

            "latency": round(random.uniform(10, 100), 2),
            "packet_loss": round(random.uniform(0, 15), 2),
            "throughput": round(random.uniform(100, 2500), 2),
            "packet_rate": round(random.uniform(5, 40), 2),

            "status": "NORMAL",
            "timestamp": time.time()
        }

    # JAMMING
    elif p < 0.85:

        radar_packet = {
            "target_id": random.randint(1, 100),
            "range": random.randint(100, 500),
            "velocity": random.randint(200, 1200),
            "signal_strength": round(random.uniform(30, 90), 2),
            "packet_size": random.randint(128, 2000),

            "latency": round(random.uniform(30, 200), 2),
            "packet_loss": round(random.uniform(3, 25), 2),
            "throughput": round(random.uniform(100, 2500), 2),
            "packet_rate": round(random.uniform(5, 35), 2),

            "status": "JAMMING",
            "timestamp": time.time()
        }

    # SUSPICIOUS
    else:

        radar_packet = {
            "target_id": random.randint(1, 100),
            "range": random.randint(100, 500),
            "velocity": random.randint(400, 1800),
            "signal_strength": round(random.uniform(40, 100), 2),
            "packet_size": random.randint(500, 3000),

            "latency": round(random.uniform(20, 150), 2),
            "packet_loss": round(random.uniform(0, 20), 2),
            "throughput": round(random.uniform(500, 4000), 2),
            "packet_rate": round(random.uniform(10, 80), 2),

            "status": "SUSPICIOUS",
            "timestamp": time.time()
        }

    radar_packet["network_health_score"] = round(
        radar_packet["signal_strength"]
        - radar_packet["packet_loss"]
        - radar_packet["latency"] / 10,
        2
    )

    radar_packet["signal_latency_ratio"] = round(
        radar_packet["signal_strength"]
        / (radar_packet["latency"] + 1),
        2
    )

    client.sendto(
        json.dumps(radar_packet).encode(),
        (HOST, PORT)
    )

    time.sleep(0.05)