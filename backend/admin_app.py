from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/admin/dashboard')
def dashboard():
    return jsonify({
        'title': 'Admin Dashboard',
        'total_users': 42,
        'active_sessions': 7,
        'service': 'admin',
        'port': 6001
    })


@app.route('/admin/users')
def users():
    return jsonify({
        'users': [
            {'id': 1, 'name': 'Alice', 'role': 'admin'},
            {'id': 2, 'name': 'Bob', 'role': 'editor'},
            {'id': 3, 'name': 'Charlie', 'role': 'viewer'}
        ],
        'service': 'admin',
        'port': 6001
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=True)
