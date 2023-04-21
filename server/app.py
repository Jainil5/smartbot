from flask import *
import requests
from flask_restful import *
import openai
app = Flask(__name__, static_url_path="",static_folder="../client/build")
api = Api(app)


@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")


@app.route('/soon')
def soon():
    return render_template('soon.html')


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route('/api/ask', methods=['POST'])
def greeting():
    data = request.get_json()
    name = data['ask']

    BASE = "http://127.0.0.1:2000/ask/"
    response = requests.get(BASE + name)
    x = response.json()
    print(x)
    #print(response.json())
    #return jsonify({str(name):str(response)})
    return jsonify({'reply': x})


if __name__ == "__main__":
    app.run(debug=True,port=5000)

