from flask import flask

app = Flask(__name__)

@route("/")
def index():
    return "It's alive."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")