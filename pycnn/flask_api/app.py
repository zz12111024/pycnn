from flask import Flask, request, jsonify
from flask_cors import CORS
from pycnn.pycnn_test import test_mydata, get_predict, get_probability

app = Flask(__name__)
CORS(app)  # 允许跨域请求


@app.route('/api/process', methods=['GET', 'POST'])
def process_data():
    if request.method == 'GET':
        test_mydata()
        probability = get_probability()
        predict = get_predict()
        return jsonify({"message": f"此手写图片值为：{predict[0]},其最大概率为：{probability}"})
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
