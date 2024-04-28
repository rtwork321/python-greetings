import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Use the port specified in the environment variable or default to 3000
    port = int(os.getenv('PORT', 3000))
    app.run(host="0.0.0.0", debug=True, port=port)
