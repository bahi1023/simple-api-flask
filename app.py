from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="health", ok=True)

@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
    return jsonify(message=text)

@app.get("/date")
def date():
    return jsonify(date=datetime.now(timezone.utc).isoformat())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
