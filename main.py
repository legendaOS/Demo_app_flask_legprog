from flask import Flask
from listToJSON import listToJSON
from User import User
from Game import Game

app = Flask(__name__)

@app.route('/how-are-you')
def haha():
    return 'iam fine!'

@app.route('/')
def main():
    return 'server works!'


players = [ User('Вася', 'Пупкин', 1), User('Петя', 'Тряпкин', 2), User('Даша', 'Корйека', 3) ]

games = [
    Game(1, 'haha'),
    Game(2, 'hehe')
]

games[0].connect(players[0])
games[0].connect(players[1])

games[1].connect(players[2])
games[1].connect(players[0])

@app.route('/users')
def playesr():
    buffer = listToJSON(players)
    return {
        'users': buffer,
        'count': len(buffer)
    }

@app.route('/games')
def games_lsdlfkjsldkfsldkfj():
    buffer = listToJSON(games)
    return {
        'games': buffer,
        'count': len(buffer)
    }


if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=3000)