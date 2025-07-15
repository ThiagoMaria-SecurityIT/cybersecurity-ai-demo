from transformers import pipeline

# Load OWASP model
owasp_clf = pipeline(
    "text-classification", 
    model="../owasp_model",
    tokenizer="../owasp_model"
)

# Sample detection
test_cases = [
    "SELECT * FROM users",
    "Normal API request",
    "<script>alert(1)</script>"
]

for text in test_cases:
    result = owasp_clf(text)
    print(f"Input: {text[:30]}... → {result[0]['label']} (Confidence: {result[0]['score']:.0%})")
