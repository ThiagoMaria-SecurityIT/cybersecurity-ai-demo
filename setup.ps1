# Clone repo
git clone https://github.com/ThiagoMaria-SecurityIT/cybersecurity-ai-demo.git
cd cybersecurity-ai-demo

# Create and activate venv
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Verify
Write-Host "`nVerification:" -ForegroundColor Green
python -c "import transformers; print(f'Transformers {transformers.__version__} installed')"
pip list

# Run demo
Write-Host "`nRun the demo:" -ForegroundColor Yellow
Write-Host "python examples/3_live_detection.py" -ForegroundColor Cyan
