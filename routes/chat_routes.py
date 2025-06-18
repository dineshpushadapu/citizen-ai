from flask import Blueprint, request, jsonify
from models.chat_model import generate_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = generate_response(user_input)
    return jsonify({"response": response})
