from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "my_verify_token"

@app.route("/")
def home():
    return "OK"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
