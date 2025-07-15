"""
OWASP Threat Classifier Trainer
-------------------------------

Automatically detects GPU/CPU and configures training accordingly:
- Uses CUDA if available (with GPU optimizations)
- Falls back to CPU with appropriate settings
- Disables GPU-specific features when running on CPU

Requirements:
pip install pandas transformers[torch] datasets accelerate
"""

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
import sys
from tqdm.auto import tqdm

# 1. Hardware Detection
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\n🔍 Detected hardware: {device.upper()}")

# 2. Load Data
try:
    print("\n📂 Loading dataset...")
    df = pd.read_json("../data/owasp10_samples.jsonl", lines=True)
    dataset = Dataset.from_pandas(df)
    label2id = {label: idx for idx, label in enumerate(set(dataset["label"]))}
    id2label = {idx: label for label, idx in label2id.items()}
except Exception as e:
    print(f"❌ Data loading failed: {e}")
    sys.exit(1)

# 3. Initialize Model
try:
    print("🧠 Loading model...")
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=len(label2id),
        id2label=id2label,
        label2id=label2id
    ).to(device)  # Send model to detected device
except Exception as e:
    print(f"❌ Model initialization failed: {e}")
    sys.exit(1)

# 4. Tokenization
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

try:
    print("✂️ Tokenizing data...")
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
    tokenized_dataset = tokenized_dataset.map(lambda x: {"labels": label2id[x["labels"]]})
except Exception as e:
    print(f"❌ Tokenization failed: {e}")
    sys.exit(1)

# 5. Training Configuration
training_args = TrainingArguments(
    output_dir="../owasp_model",
    per_device_train_batch_size=8 if device == "cuda" else 4,  # Smaller batch for CPU
    num_train_epochs=3,
    save_strategy="epoch",
    dataloader_pin_memory=(device == "cuda"),  # Only enable for GPU
    no_cuda=(device != "cuda"),                # Explicitly disable CUDA if not available
    report_to="none",
    logging_steps=10,
    disable_tqdm=False
)

# 6. Training Execution
try:
    print(f"\n🚀 Training on {device.upper()}...")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    
    with tqdm(total=training_args.num_train_epochs, desc="Training") as pbar:
        trainer.train()
        pbar.update(training_args.num_train_epochs)
    
    trainer.save_model("../owasp_model")
    tokenizer.save_pretrained("../owasp_model")
    print("\n✅ Training completed successfully!")
except Exception as e:
    print(f"❌ Training failed: {e}")
    sys.exit(1)
