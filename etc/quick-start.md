# **Cybersecurity AI Demo - Quickstart Guide**

## 📜 Index
1. **Setup Instructions**
2. **File Overview**
3. **Execution Flow** 
4. **Expected Results**
5. **Missing Requirements**

---

## 1. 🛠️ Setup Instructions
```bash
# Clone and run (All platforms)
git clone https://github.com/your-repo.git
cd cybersecurity-ai-demo

# Choose your OS script:
./setup.sh       # Linux/Mac
.\setup.ps1      # Windows PowerShell
.\setup.bat      # Windows CMD
```

---

## 2. 📂 File Overview
| File | Purpose | Output |
|------|---------|--------|
| `data/owasp10_samples.jsonl` | OWASP attack samples | Training data for model 1 |
| `data/cvss4_samples.jsonl` | CVSS vulnerability data | Training data for model 2 |
| `examples/1_owasp_classifier.py` | Trains OWASP threat detector | Generates `owasp_model/` |
| `examples/2_cvss_predictor.py` | Trains CVSS score predictor | Generates `cvss_model.joblib` |
| `examples/3_live_detection.py` | Runs live threat detection | Terminal output |

---

## 3. ▶️ Execution Flow
```mermaid
graph LR
    A[1_owasp_classifier.py] --> B[owasp_model/]
    C[2_cvss_predictor.py] --> D[cvss_model.joblib]
    B & D --> E[3_live_detection.py]
```

1. **First Run**:  
   ```bash
   python examples/1_owasp_classifier.py
   ```
   - *Expected*: Creates `owasp_model/` folder with `.bin` and `config.json`

2. **Second Run**:  
   ```bash
   python examples/2_cvss_predictor.py
   ```
   - *Expected*: Generates `cvss_model.joblib` file

3. **Demo**:  
   ```bash
   python examples/3_live_detection.py
   ```
   - *Expected*: Prints threat analysis like:
     ```
     Input: "SELECT * FROM users" → SQLi (92% confidence)
     Input: "<script>alert(1)" → XSS (95% confidence)
     ```

---

## 4. ✔️ Expected Results
- Successful runs will create:
  - `owasp_model/` directory
  - `cvss_model.joblib` file
- Demo script should output:
  - Threat classifications (SQLi/XSS/Benign)
  - CVSS score predictions (0-10 scale)

---

## 5. ⚠️ Missing Requirements
To run **without errors**, you need:

1. **Data Validation**:
   - Confirm `data/*.jsonl` files contain:
     ```json
     {"text": "malicious payload", "label": "SQLi"}
     {"description": "RCE bug", "cvss_score": 9.8, "metrics": {...}}
     ```

2. **File Dependencies**:
   - `owasp_model/` must contain:
     - `config.json`
     - `pytorch_model.bin`
   - `cvss_model.joblib` must exist

3. **Environment**:
   ```bash
   pip install transformers scikit-learn datasets
   ```

4. **Asset Generation** (Optional):
   - Install `asciinema` for GIF creation:
     ```bash
     pip install asciinema
     ```

---

## 🚨 Troubleshooting
If errors occur:
1. Verify virtual environment is activated
2. Check `data/` files have valid JSONL format
3. Ensure all scripts run from repo root  


This warning occurs because you're trying to use GPU memory pinning (`pin_memory=True`) but don't have a CUDA-enabled GPU available. Here's how to fix it:

### **Solution 1: Disable pin_memory (Recommended for CPU-only)**
Modify your `TrainingArguments` in `1_owasp_classifier.py`:
```python
training_args = TrainingArguments(
    output_dir="../owasp_model",
    per_device_train_batch_size=8,
    num_train_epochs=3,
    save_strategy="epoch",
    dataloader_pin_memory=False  # Add this line
)
```

### **Solution 2: If you have a GPU**
1. Install CUDA-compatible PyTorch:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

2. Verify GPU availability:
```python
import torch
print(torch.cuda.is_available())  # Should return True
```

### **Why This Happens**
- `pin_memory=True` is default in Hugging Face to speed up GPU transfers
- Without a GPU, this setting has no effect
- The warning is harmless but can be silenced

### **Updated Full Code**
```python
training_args = TrainingArguments(
    output_dir="../owasp_model",
    per_device_train_batch_size=8,
    num_train_epochs=3,
    save_strategy="epoch",
    dataloader_pin_memory=False,  # Disabled for CPU
    no_cuda=not torch.cuda.is_available()  # Automatically detect GPU
)
```

This change:
- Silences the warning
- Maintains functionality
- Works for both CPU and GPU environments
