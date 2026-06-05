import csv
import os

CSV_FILE = "data/radar_traffic.csv"


def initialize_csv():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "target_id",
                "range",
                "velocity",
                "signal_strength",
                "packet_size"
            ])


def log_packet(packet):

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            packet["timestamp"],
            packet["target_id"],
            packet["range"],
            packet["velocity"],
            packet["signal_strength"],
            packet["packet_size"]
        ])