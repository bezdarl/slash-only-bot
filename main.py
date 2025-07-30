from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Slash-only бот на Render работает!"

@app.route("/interactions", methods=["POST"])
def interactions():
    data = request.json
    if data.get("type") == 1:
        return jsonify({"type": 1})  # Discord PING
    if data.get("type") == 2 and data["data"]["name"] == "testspam":
        return jsonify({
            "type": 4,
            "data": {
                "content": "✅ Slash-only бот отвечает с Render!"
            }
        })
    return jsonify({})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
