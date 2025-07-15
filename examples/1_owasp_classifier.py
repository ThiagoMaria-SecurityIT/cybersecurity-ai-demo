from transformers import pipeline
from datasets import load_dataset

# Load sample data
dataset = load_dataset("json", data_files="../data/owasp10_samples.jsonl", split="train")

# Train a simple classifier
classifier = pipeline("text-classification", model="distilbert-base-uncased")
classifier.fit(dataset["text"], dataset["label"])

# Test prediction
result = classifier("admin'--")
print(f"Detected: {result[0]['label']} (Confidence: {result[0]['score']:.0%})")
