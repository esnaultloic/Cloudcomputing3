import os
from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

model_path = "./distilbert-base-uncased-finetuned-sst-2-english"

@app.route('/')
def classify_review():
    review = request.args.get('review')
    api_key = request.args.get('api_key')
    if review is None or api_key != "MyCustomerApiKey":
        return jsonify(code=403, message="bad request")
    classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    return classify("that was great")[0]


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
