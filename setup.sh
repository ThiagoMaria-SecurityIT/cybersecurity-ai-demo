#!/bin/bash
git clone https://github.com/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Ready! Run: python examples/3_live_detection.py"
