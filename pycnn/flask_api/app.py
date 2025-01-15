from flask import Flask, request, jsonify
from flask_cors import CORS
from pycnn.pycnn_test import test_mydata as test

app = Flask(__name__)
CORS(app)  # 允许跨域请求


@app.route('/api/process', methods=['GET', 'POST'])
def process_data():
    if request.method == 'GET':
        test()
        return jsonify({"message": "This is a GET response."})
    elif request.method == 'POST':
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input"}), 400
        return jsonify({"message": f"Hello, {data['name']}! This is a Python backend response."})


@app.route('/')
def home():
    return 'Welcome to the Flask API'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
