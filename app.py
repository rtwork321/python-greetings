from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':

    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        # Default port
        port = 3000

    app.run(host="0.0.0.0", debug=True, port=port)