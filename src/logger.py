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
                "packet_size",
                "latency",
                "packet_loss",
                "throughput",
                "packet_rate",
                "network_health_score",
                "signal_latency_ratio",
                "status"
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
            packet["packet_size"],
            packet["latency"],
            packet["packet_loss"],
            packet["throughput"],
            packet["packet_rate"],
            packet["network_health_score"],
            packet["signal_latency_ratio"],
            packet["status"]
        ])