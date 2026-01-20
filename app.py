from flask import Flask, render_template, request
import os

app = Flask(__name__)

chat_history = []

def chatbot_response(u):
    u = u.lower().strip()

    if u == "hi":
        return "Hello!"
    elif u == "hello":
        return "Hi there!"
    elif u == "how are you":
        return "I'm doing great!"
    elif u == "bye":
        return "Goodbye! (refresh page to start again)"
    else:
        return "I don't understand."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("message")
        bot_reply = chatbot_response(user_input)

        chat_history.append(("user", user_input))
        chat_history.append(("bot", bot_reply))

    return render_template("index.html", chats=chat_history)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

