from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_gamer():
    return "Hello Gamer!"
