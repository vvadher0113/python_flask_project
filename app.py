from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    name = None

    if request.method == "POST":
        name = request.form.get("name")

    return render_template("index.html", name=name)


@app.route("/health")
def health():
    return {"status": "healthy"}
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)