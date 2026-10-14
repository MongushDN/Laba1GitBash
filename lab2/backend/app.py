from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Разрешаем фронтенду обращаться к бэкенду

@app.route('/ping', methods=['GET'])
def ping():
    today = datetime.now().strftime("%d.%m.%Y")
    return jsonify({
        "message": "My response!",
        "date": today,
        "pong": f"Today is {today}"
    })

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Backend is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)