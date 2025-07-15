from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
import torch

# Load data
dataset = load_dataset("json", data_files="../data/owasp10_samples.jsonl", split="train")

# Tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", 
    num_labels=len(set(dataset["label"]))
)

# Training loop (simplified)
inputs = tokenizer(dataset["text"], padding=True, truncation=True, return_tensors="pt")
labels = torch.tensor([{"SQLi": 0, "XSS": 1, "Benign": 2}[x] for x in dataset["label"]])

# Save model
model.save_pretrained("../owasp_model")
tokenizer.save_pretrained("../owasp_model")
