
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/bitrix24', methods=['POST'])
def handle_bitrix24():
    data=request.json
    return jsonify(data)
