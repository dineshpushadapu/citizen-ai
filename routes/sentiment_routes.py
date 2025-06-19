from flask import Blueprint, request, jsonify
from models.sentiment_model import analyze_sentiment
from utils.text_cleaning import clean_text

sentiment_bp = Blueprint("sentiment", __name__)

@sentiment_bp.route("/sentiment", methods=["POST"])
def sentiment():
    message = request.json.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    cleaned = clean_text(message)
    sentiment = analyze_sentiment(cleaned)
    return jsonify({"sentiment": sentiment})


