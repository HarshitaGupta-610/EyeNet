from datetime import datetime

LOG_FILE = "logs/alerts.log"


def generate_alert(prediction, packet):

    if prediction == "NORMAL":
        return

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    alert_message = (
        f"[{timestamp}] "
        f"{prediction} | "
        f"Target={packet['target_id']} | "
        f"Signal={packet['signal_strength']} | "
        f"Loss={packet['packet_loss']} | "
        f"Latency={packet['latency']}\n"
    )

    print("\n🚨 ALERT")
    print(alert_message)

    with open(
        LOG_FILE,
        "a"
    ) as file:

        file.write(alert_message)