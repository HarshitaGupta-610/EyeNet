import joblib
import pandas as pd

model = joblib.load(
    "models/eyenet_model.pkl"
)


def predict_packet(packet):

    data = pd.DataFrame([
        {
            "range":
                packet["range"],

            "velocity":
                packet["velocity"],

            "signal_strength":
                packet["signal_strength"],

            "packet_size":
                packet["packet_size"],

            "latency":
                packet["latency"],

            "packet_loss":
                packet["packet_loss"],

            "throughput":
                packet["throughput"],

            "packet_rate":
                packet["packet_rate"],

            "network_health_score":
                packet["network_health_score"],

            "signal_latency_ratio":
                packet["signal_latency_ratio"]
        }
    ])

    prediction = model.predict(data)[0]

    return prediction