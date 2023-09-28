from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<string:name1>/")
def say_hello(name1):
    return f"Hello {name1}!"


if __name__ == "__main__":
    app.run()