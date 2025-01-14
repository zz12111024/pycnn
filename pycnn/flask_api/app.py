from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run-python', methods=['POST'])
def run_python():
    try:
        data = request.json
        input_value = data.get('input', 'default value')

        # 使用 format 替代 f-strings
        result = "The message you send is: {}".format(input_value)

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
