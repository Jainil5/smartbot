from flask import *
import requests
from flask_restful import *
app = Flask(__name__, static_url_path="",static_folder="../client/build")
api = Api(app)
import csv
l = []
@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")

@app.route('/soon')
def soon():
    return render_template('soon.html')

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/query")
def query():
    return render_template("t2q.html")

@app.route("/explain")
def explain():
    return render_template("codeexp.html")

@app.route('/api/csv', methods=['POST'])
def csv_api():
    headers = request.json['headers']
    print(headers)
    l.append(headers)
    # Process the CSV headers as needed
    response_data = {'message': 'CSV headers received'}
    return jsonify(response_data)

@app.route('/api/ask', methods=['POST'])
def api():
    data = request.get_json()
    if len(l)!=0:
        pre = "Table with properties: " + str(l) + "generate query "
        input = data['ask']
        send = pre + str(input)
        BASE = "http://127.0.0.1:2000/ask/"
        response = requests.get(BASE + send)
        x = response.json()
        print(x)
        #print(response.json())
        #return jsonify({str(name):str(response)})
        return jsonify({'reply': x})





if __name__ == "__main__":
    app.run(debug=True)
