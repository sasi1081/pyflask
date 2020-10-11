from flask import Flask,request,jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

myapplication =  [
{
'version': '1.0',
'lastcommitsha': 'abc57858585',
'description' : 'pre-interview technical test'
}
]

@app.route('/' ,  methods=['GET'])
def home():
    return "<h1>Hello , Greetings from Sasi!</p>"

@app.route('/version', methods=['GET'])

def api_all():
    return jsonify(myapplication)


if __name__ == "__main__":
    app.run(host='127.0.0.1')
