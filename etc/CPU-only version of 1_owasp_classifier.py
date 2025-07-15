from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
import sys

# Check for required packages
try:
    import accelerate
    assert accelerate.__version__ >= '0.26.0', "accelerate>=0.26.0 required"
except (ImportError, AssertionError) as e:
    print(f"Error: {e}\nPlease run: pip install 'accelerate>=0.26.0'")
    sys.exit(1)

# 1. Load and prepare data
try:
    df = pd.read_json("../data/owasp10_samples.jsonl", lines=True)
    dataset = Dataset.from_pandas(df)
except Exception as e:
    print(f"Data loading failed: {e}")
    sys.exit(1)

# 2. Initialize model and tokenizer
model_name = "distilbert-base-uncased"
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Convert text labels to numerical IDs
    label2id = {label: idx for idx, label in enumerate(set(dataset["label"]))}
    id2label = {idx: label for label, idx in label2id.items()}

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=len(label2id),
        id2label=id2label,
        label2id=label2id
    )
except Exception as e:
    print(f"Model initialization failed: {e}")
    sys.exit(1)

# 3. Tokenization function
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

# 4. Process dataset
try:
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
    tokenized_dataset = tokenized_dataset.map(lambda x: {"labels": label2id[x["labels"]]})
except Exception as e:
    print(f"Tokenization failed: {e}")
    sys.exit(1)

# 5. CPU-optimized training setup
training_args = TrainingArguments(
    output_dir="../owasp_model",
    per_device_train_batch_size=4,  # Reduced for CPU
    num_train_epochs=3,
    save_strategy="epoch",
    dataloader_pin_memory=False,    # Disabled for CPU
    no_cuda=True,                   # Force CPU
    report_to="none"                # Disable logging
)

# 6. Train and save
try:
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    print("Training started...")
    trainer.train()
    trainer.save_model("../owasp_model")
    tokenizer.save_pretrained("../owasp_model")
    print("Training completed successfully!")
except Exception as e:
    print(f"Training failed: {e}")
    sys.exit(1)
