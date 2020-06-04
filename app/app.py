from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_gamer():
    return "Hello Gamer!"


@app.route('/addGame')
def add_game():
    return "Add Game Endpoint"


@app.route('/listGames')
def list_games():
    return "list of games"


@app.route('/removeGame')
def remove_game():
    return "Game Removed"
