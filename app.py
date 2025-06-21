from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# Fetch the Mongo URI
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client.chatdb  # Database
messages = db.messages  # Collection


@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    messages.insert_one(data)
    return jsonify({"status": "Message stored"}), 201


@app.route('/messages', methods=['GET'])
def get_messages():
    result = list(messages.find({}))
    return jsonify(result)

@app.route("/")
def home():
    return render_template('/home.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7000)