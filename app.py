from flask import Flask, request
from ie_utils import tokenize


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args.get("sentence","")
    lower = bool(request.args.get("lower", False))
    try:
        return str(tokenize(sentence, lower = lower))
    except ValueError:
        return "[]"
    
    

    