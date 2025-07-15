import gradio as gr
def detect_threat(text):
    return {"SQLi": 0.92, "XSS": 0.15}  # Mock results
gr.Interface(detect_threat, "textbox", "label").launch()
