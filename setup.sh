#!/bin/bash
# Clone repo
git clone https://github.com/cybersecurity-ai-demo.git
cd your-repo

# Create and activate venv
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Verify
echo -e "\nVerification:"
python -c "import transformers; print(f'Transformers {transformers.__version__} installed')"
pip list

# Run instructions
echo -e "\nRun the demo:"
echo "python examples/3_live_detection.py"
