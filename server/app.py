from flask import Flask, render_template, Response, request, send_from_directory
import requests
from form import Form

app = Flask(__name__, static_url_path="",static_folder="../client/build")


@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")


@app.route('/soon')
def soon():
    return render_template('soon.html')


@app.route("/chat")
def chat():
    return render_template("chat.html")


if __name__ == "__main__":
    app.run(debug=True)

