import socket
import json

from logger import initialize_csv
from logger import log_packet

from predict import predict_packet
from alert_system import generate_alert

from stats import update_stats

HOST = "127.0.0.1"
PORT = 9999

initialize_csv()

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

server.bind((HOST, PORT))

print("EyeNet Receiver Started")
print(f"Listening on {HOST}:{PORT}")

while True:

    data, addr = server.recvfrom(4096)

    packet = json.loads(
        data.decode()
    )

    prediction = predict_packet(
        packet
    )

    update_stats(
        prediction
    )

    generate_alert(
        prediction,
        packet
    )

    log_packet(
        packet
    )