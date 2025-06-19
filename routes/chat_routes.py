# routes/chat_routes.py

from flask import Blueprint, request, jsonify
from models.chat_model import generate_response
from utils.text_cleaning import clean_text

# Blueprint for the chat route
chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    # Get message from request
    user_input = request.json.get("message", "")
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Clean the input and generate a response
    cleaned_input = clean_text(user_input)
    response = generate_response(cleaned_input)

    return jsonify({"response": response})
