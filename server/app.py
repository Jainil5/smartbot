from flask import Flask, render_template, Response, request, send_from_directory
import requests
from form import Form
from flask_restful import *
import openai
openai.api_key = "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"
app = Flask(__name__, static_url_path="",static_folder="../client/build")
api = Api(app)

def reply(x):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": x}])
    reply =completion["choices"][0]["message"]["content"]
    return reply

@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")


@app.route('/soon')
def soon():
    return render_template('soon.html')


@app.route("/chat")
def chat():
    print("Chat:"+"/chat")
    return render_template("chat.html")

class API(Resource):
    def get(self,data):
        answer = reply(str(data))
        return answer

api.add_resource(API,"/ask/<string:data>")


if __name__ == "__main__":
    app.run(debug=True)

