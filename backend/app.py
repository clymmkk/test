from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import platform
import sys

app = Flask(__name__)
CORS(app)


@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello from Flask Main Service!',
        'service': 'main',
        'port': 6000
    })


@app.route('/api/time')
def get_time():
    return jsonify({
        'current_time': datetime.datetime.now().isoformat(),
        'service': 'main',
        'port': 6000
    })


@app.route('/api/info')
def get_info():
    return jsonify({
        'python_version': sys.version,
        'platform': platform.platform(),
        'service': 'main',
        'port': 6000
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
