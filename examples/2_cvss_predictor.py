import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from joblib import dump

# Load and prepare data
df = pd.read_json("../data/cvss4_samples.jsonl", lines=True)
X = pd.json_normalize(df["metrics"])  # Flatten nested JSON
y = df["cvss_score"]

# Train and save
model = RandomForestRegressor()
model.fit(X, y)
dump(model, "../cvss_model.joblib") 
