from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for uploaded files metadata
uploaded_files = []


@app.route('/upload/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_info = {
        'filename': file.filename,
        'content_type': file.content_type,
        'size': len(file.read())
    }
    uploaded_files.append(file_info)
    return jsonify({
        'message': 'File uploaded successfully',
        'file': file_info,
        'service': 'upload',
        'port': 6002
    })


@app.route('/upload/files')
def list_files():
    return jsonify({
        'files': uploaded_files,
        'service': 'upload',
        'port': 6002
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6002, debug=True)
