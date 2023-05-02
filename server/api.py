from flask import *
from flask_restful import *
import openai
import requests

app = Flask(__name__)
api = Api(app)
openai.api_key = ""
a = "xsk-DCqjESAZsRHVdEmuiyQ0T3BlbkFJFZij5fzmcVeRsj2sPwXHx"

match = ["change volume to","set volume to"]

def reply(x):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": x}])
    reply =completion["choices"][0]["message"]["content"]
    return reply

class query(Resource):
    def get(self,ask):
        print(ask)       
        print("\n",reply(ask))
        return str(reply(ask))

api.add_resource(query,"/ask/<string:ask>")





if __name__ == "__main__":
    app.run(debug=True,port=2000)