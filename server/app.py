from flask import Flask, render_template, Response, request, send_from_directory
from appf import *
import requests


app = Flask(__name__, static_url_path="",static_folder="../client/build")



@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")

@app.route('/soon')
def soon():
    return render_template('soon.html')

@app.route("/Chat")
def chat():
    return render_template("chat.html")

@app.route("/HowToUse")
def howto():
    return render_template("chat.html")

@app.route('/chat', methods=['GET'])
def process_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Do something with the user input
    # ...
    print(name)

    return 'Form submitted successfully'


if __name__ == "__main__":
    app.run(debug=True)

