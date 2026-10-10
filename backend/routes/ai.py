import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify

ai_bp = Blueprint("ai", __name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash-latest"
)

@ai_bp.route("/api/ai/chat", methods=["POST"])
def ai_chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message required"}), 400

    user_message = data["message"]

    response = model.generate_content(user_message)

    return jsonify({
        "reply": response.text
    })