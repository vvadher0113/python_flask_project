from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="My Flask Website")


@app.route("/hello")
def hello():
    name = request.args.get("name", "Learner")
    return f"Hello, {name}! Welcome to Flask."


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "message": "Flask app is running"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)