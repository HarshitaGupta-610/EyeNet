import pandas as pd

df = pd.read_csv("data/radar_traffic.csv")

print("Total Rows:", len(df))

print("\nClass Distribution:\n")
print(df["status"].value_counts())