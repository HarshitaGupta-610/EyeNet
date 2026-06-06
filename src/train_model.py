import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv("data/radar_traffic.csv")

X = df[
    [
        "range",
        "velocity",
        "signal_strength",
        "packet_size",
        "latency",
        "packet_loss",
        "throughput",
        "packet_rate",
        "network_health_score",
        "signal_latency_ratio"
    ]
]

y = df["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    )
}

best_model = None
best_name = ""
best_accuracy = 0

print("\nMODEL COMPARISON\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print(f"{name}: {acc:.4f}")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_name = name

print("\nBEST MODEL:", best_name)
print("ACCURACY:", round(best_accuracy, 4))

predictions = best_model.predict(X_test)

print("\nCLASSIFICATION REPORT\n")
print(classification_report(y_test, predictions))

print("\nCONFUSION MATRIX\n")
print(confusion_matrix(y_test, predictions))

if hasattr(best_model, "feature_importances_"):

    print("\nFEATURE IMPORTANCE\n")

    importance_data = sorted(
        zip(X.columns, best_model.feature_importances_),
        key=lambda x: x[1],
        reverse=True
    )

    for feature, score in importance_data:
        print(f"{feature:<25} {score:.4f}")

joblib.dump(
    best_model,
    "models/eyenet_model.pkl"
)

print("\nModel Saved Successfully")