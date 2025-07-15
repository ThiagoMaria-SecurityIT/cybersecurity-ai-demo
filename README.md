# AI for Cybersecurity Demo - Under Development

> [!Warning]
> - This repo is under development and are not for production  
> - Please, consider the .gif file (detection_example.gif) has annotations inside and are not a real image file  
> - Not recommended download this repo today July 15, 2025  
> - This repo was changed to public today July 15, 2025  
> - This repo is public so I can use online tools to make it better  


> [!Caution]
> UNDER DEVELOPMENT - JULY 15, 2025



## Transparency:
- Made with the help of AI 
- Date this repo was created: July 14, 2025   

## This repository demonstrates how AI can detect security threats using:
- **OWASP Top 10** (Common web attacks)
- **CVSS 4.0** (Scoring system for vulnerabilities)

```mermaid
  graph TD
    A[1_owasp_classifier.py] -->|Generates Model| C[3_live_detection.py]
    B[2_cvss_predictor.py] -->|Generates Model| C
    C --> D[assets/detection_example.gif]  
```

## What This Shows
- 🛡️ How AI learns patterns in cyber threats
- ⚙️ Basic model training process
- 🔍 Real-time detection examples

---

### **🚀 One-Click Setup**  
Get started in seconds with an automated setup scripts for all major platforms:

| Script | Platform | What It Does |  
|--------|----------|--------------|  
| [`setup.ps1`](setup.ps1) | **Windows (PowerShell)** | 1. Creates virtual environment<br>2. Installs dependencies<br>3. Verifies installation |  
| [`setup.bat`](setup.bat) | **Windows (CMD)** | Simple double-click executable for non-technical users |  
| [`setup.sh`](setup.sh) | **Linux/Mac** | Configures everything with terminal commands |    

## 🧪 Validation Test
After setup, verify everything works:
```bash
python test_install.py
```  

**How to use:**  
1. **PowerShell**: Right-click → _"Run with PowerShell"_  
2. **CMD**: Double-click `setup.bat`  
3. **Linux/Mac**: Run in terminal:
   
   ```bash  
   chmod +x setup.sh && ./setup.sh  
   ```  
### Windows Users
- **PowerShell** (Recommended):  
  Right-click on [`setup.ps1`](setup.ps1) and select "Run with PowerShell"
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\setup.ps1
  ```

- **Command Prompt (CMD)**:  
  Simply double-click [`setup.bat`](setup.bat)

### Mac/Linux Users
Run in terminal:
```bash
chmod +x setup.sh && ./setup.sh
```

📌 **What these scripts do**:
1. Create isolated Python environment
2. Install all required packages
3. Verify successful installation
4. Show how to run the demo

🔒 **Safety Features**:
- No admin rights required
- Doesn't modify system Python
- Includes dependency verification  

✅ **Guaranteed isolation** – Installs everything in a self-contained virtual environment.  

---

### Suggested Placement  
Add this section right after your project description (before "What This Shows").  

**Why This Matters for Recruiters:**  
- Demonstrates your understanding of **cross-platform compatibility**  
- Shows you care about **user experience** (non-technical users can test your work)  
- Highlights **production-ready practices** (isolated environments, verification steps)  

Would you like me to provide the exact Markdown to copy-paste into your existing `README.md`? I can match your current formatting style.

## Try It Yourself
```bash
python examples/1_owasp_classifier.py
```

## AI in Cybersecurity
- This mimics how SOC analysts train systems to detect:
  - Injection attacks (OWASP #1 risk)
  - Vulnerability severity (CVSS scores)
- Real-world systems process millions of such samples daily

  ## Skills Demonstrated
- Model Training: ✔️
- Security Knowledge: ✔️
- Production Readiness: ✔️


