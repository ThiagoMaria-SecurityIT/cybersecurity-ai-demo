#!/usr/bin/env python3
"""
VALIDATION SCRIPT FOR CYBERSECURITY DEMO
Run after setup.sh/setup.ps1 to verify installation
"""

import os
import json
import joblib
from transformers import pipeline, AutoModel

def check_files():
    """Verify critical files exist"""
    required = [
        'data/owasp10_samples.jsonl',
        'data/cvss4_samples.jsonl',
        'owasp_model/config.json',
        'cvss_model.joblib'
    ]
    
    missing = [f for f in required if not os.path.exists(f)]
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    return True

def test_owasp_model():
    """Quick test of OWASP classifier"""
    try:
        classifier = pipeline("text-classification", model="./owasp_model")
        sample = "SELECT * FROM users"
        result = classifier(sample)[0]
        print(f"✅ OWASP test: '{sample[:15]}...' → {result['label']} (score: {result['score']:.2f})")
        return True
    except Exception as e:
        print(f"❌ OWASP model failed: {str(e)}")
        return False

def test_cvss_model():
    """Quick test of CVSS predictor"""
    try:
        model = joblib.load("cvss_model.joblib")
        # Mock features matching training data structure
        test_features = {'attack_vector': 1, 'complexity': 0}  
        prediction = model.predict([list(test_features.values())])[0]
        print(f"✅ CVSS test: Predicted score = {prediction:.1f}/10")
        return True
    except Exception as e:
        print(f"❌ CVSS model failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n🔍 Validating Cybersecurity Demo Setup")
    files_ok = check_files()
    owasp_ok = test_owasp_model() if files_ok else False
    cvss_ok = test_cvss_model() if files_ok else False
    
    if all([files_ok, owasp_ok, cvss_ok]):
        print("\n🎉 All systems operational! Run:")
        print("python examples/3_live_detection.py")
    else:
        print("\n⚠️  Validation failed. Check:")
        print("- Did setup scripts run completely?")
        print("- Are data files properly formatted?")
        print("- Check error messages above")
