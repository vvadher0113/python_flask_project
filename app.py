from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="10.0.0.4",
        user="flaskuser",
        password="flaskpassword",
        database="flaskdb"
    )


@app.route("/", methods=["GET", "POST"])
def home():
    name = None

    if request.method == "POST":
        name = request.form.get("name")

    return render_template("index.html", name=name)


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/api/status")
def api_status():
    return {
        "app": "Flask Learning Website",
        "version": "1.0",
        "status": "running"
    }


@app.route("/api/db-test")
def db_test():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT DATABASE();")
        database_name = cursor.fetchone()

        cursor.close()
        connection.close()

        return {
            "status": "success",
            "database": database_name[0]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    