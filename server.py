from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve the HTML form
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Handle form submission
@app.route('/apply', methods=['POST'])
def apply():
    form_data = request.json
    return jsonify({'outcome': 'Approved'})

if __name__ == '__main__':
    app.run(port=3000, debug=True)