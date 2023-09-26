from flask import Flask, render_template

app = Flask(__name__)
# route that user uses to request resources from
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heloo")
def heloo():
    return "Welcome to my app."

@app.route("/about")
def ded():
    return "We are dedicated to providing quality expirience"

app.run()