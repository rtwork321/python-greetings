import argparse
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=3000, help='Port number for the Flask application')
    args = parser.parse_args()
    
    app.run(host="0.0.0.0", debug=True, port=args.port)
