from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Cloud Computing Lab"


@app.route("/Student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and Devops"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=5000, debug=True)
