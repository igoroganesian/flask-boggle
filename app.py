from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}.

        >>> game_id = str(uuid4())
        >>> game = BoggleGame()
        >>> games[game_id] = game
        >>> print('game_id :', game_id)
        >>> print('board :', game.board)
        >>> print('games :', games)

    """

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return jsonify(gameId=game_id, board=game.board)

@app.post("/api/score-word")
def score_word():
    """accepts POST request with JSON for game id & word; checks if word is
    legal through:

    #is_word_in_word_list
    #check_word_on_board

    returns JSON response with jsonify():

    if not a word: {result: "not-word"}
    if not on board: {result: "not-on-board"}
    if a valid word: {result: "ok"}

    *POST form data is submitted to server as form-data, sent to request.form
    *JSON data sent via AJAX appears in request.json

    * or await axios.post("/api/score-word", { /* your data goes here... */ } )
   ?? await axios.post("/api/score-word", { "word"=word, "gameId"=gameId } )
    """

    word = request.json["word"]
    gameId = request.json["gameId"]

    game = BoggleGame()

    if not game.is_word_in_word_list(word):
        jsonify(result="not-word")
    elif not game.check_word_on_board(word):
        jsonify(result="not-on-board")
    else:
        jsonify(result="ok")







