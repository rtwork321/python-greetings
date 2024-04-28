from flask import Flask, jsonify
import argparse

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, required=True, help='Port number for the Flask app')
    args = parser.parse_args()

    # Run the Flask app on the specified port
    app.run(host="0.0.0.0", debug=True, port=args.port)
