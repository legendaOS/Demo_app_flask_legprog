from flask import Flask
from flask import request

from listToJSON import listToJSON
from User import User
from Game import Game

app = Flask(__name__)

@app.route('/')
def main():
    return 'server works!'


players = [ User('Вася', 'Пупкин', 0), User('Петя', 'Тряпкин', 1), User('Даша', 'Корйека', 2) ]

games = [
    Game(1, 'haha'),
    Game(2, 'hehe')
]

games[0].connect(players[0])
games[0].connect(players[1])

games[1].connect(players[2])
games[1].connect(players[0])



cats_names = ['Вася', 'Мурзик', 'Жирунчик', 'Вапек']


@app.route('/cats', methods = ['GET'])
def cats():
    return {
        'count': len(cats_names),
        'cats': cats_names
    }

@app.route('/cat/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cat_id(id):
    id = int(id)

    if request.method == "GET":
        return cats_names[id]
    
    elif request.method == "PUT":
        data = request.json
        cats_names[id] = data['name']
        return {
            'id': id,
            'name': cats_names[id]
        }
    
    elif request.method == 'DELETE':
        buffer_name = cats_names[id]
        cats_names.pop(id)
        return {
            'id': id,
            'name': buffer_name
        }


@app.route('/cat', methods = ['POST'])
def cat():
    if request.method == 'POST':
        data = request.json
        cats_names.append(data['name'])
        return {
            'id': len(cats_names) - 1,
            'name': data['name']
        }



if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=3000)