from flask import Blueprint, request, jsonify
from app.services.bert import pregunta_respuesta  # Import the model function

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "¡Hola, Bounsic-back está funcionando!"

@main.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    response = pregunta_respuesta(question)  # Use model function
    return jsonify(response)
