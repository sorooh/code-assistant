
from flask import Flask, request, jsonify
from gpt_handler import ask_gpt
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")
    response = ask_gpt(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
