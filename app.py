from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# tokenizer model load (sementara dulu nanti pake local model yang lebih banyak)
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"  # model ini ada classification head kiw kiw
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.softmax(outputs.logits, dim=1)
    sentiment_labels = ["very negative", "negative", "neutral", "positive", "very positive"]  # 
    
    confidences = {
        label: float(probabilities[0][i]) 
        for i, label in enumerate(sentiment_labels)
    }
    
    predicted_label = max(confidences, key=confidences.get)
    return predicted_label, confidences

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            label, confidences = predict_sentiment(text)
            result = {
                'text': text,
                'label': label,
                'confidences': confidences
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
