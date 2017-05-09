from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
    with open("data.json") as f:
        content = json.load(f)
        return jsonify(movies=content)

if __name__ == "__main__":
    app.run()