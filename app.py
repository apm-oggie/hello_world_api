from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/hello', methods=['GET'])
def hello():
    language = request.args.get('language', default='English', type=str)
    greetings = {
        'English': 'Hello world',
        'French': 'Bonjour le monde',
        'Hindi': 'Namastey sansar'
    }
    return jsonify(message=greetings.get(language, greetings['English']))  # Default to English

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 