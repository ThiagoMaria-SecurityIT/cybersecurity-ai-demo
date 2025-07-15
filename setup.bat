@echo off
:: Clone repo
git clone https://github.com/ThiagoMaria-SecurityIT/cybersecurity-ai-demo.git
cd 

:: Create and activate venv
python -m venv venv
call venv\Scripts\activate.bat

:: Install requirements
pip install -r requirements.txt

:: Verify
python -c "import transformers; print(f'Transformers {transformers.__version__} installed')"
pip list

:: Run instructions
echo.
echo Run the demo:
echo python examples/3_live_detection.py
pause
