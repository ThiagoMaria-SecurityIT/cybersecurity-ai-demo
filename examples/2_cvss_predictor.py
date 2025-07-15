import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load CVSS data
df = pd.read_json("../data/cvss4_samples.jsonl", lines=True)

# Train score predictor
model = RandomForestRegressor()
model.fit(pd.json_normalize(df["metrics"]), df["cvss_score"])

# Predict new vulnerability
new_case = [{"attack_vector": "Network", "complexity": "Low"}]
pred_score = model.predict(new_case)[0]
print(f"Predicted CVSS 4.0 Score: {pred_score:.1f}")
