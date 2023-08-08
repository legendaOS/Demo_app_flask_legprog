from flask import Flask
from flask import request

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


players = [ User('Вася', 'Пупкин', 0), User('Петя', 'Тряпкин', 1), User('Даша', 'Корйека', 2) ]

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

cats_names = ['Вася', 'Мурзик', 'Жирунчик', 'Вапек']
cats_info = {
    'Вася': 'дворняга', 
    'Мурзик': 'домашний', 
    'Жирунчик': 'сфинкс', 
    'Вапек': 'британский'
}

@app.route('/cats')
def cats():
    return cats_names

@app.route('/cat/<number>')
def cat(number):
    number = int(number)
    if number < 0 or number > len(cats_names):
        return 'неверный индекс!'
    else:
        return cats_names[number]

@app.route('/cat_info/<name>')
def cat_info(name):
    if name in cats_info.keys():
        return cats_info[name]
    else:
        return 'ошибка ключа!'
    

@app.route('/create_user')
def create_user():
    buffer_name = request.args.get('name')
    buffer_sname = request.args.get('sname')

    new_user = User(buffer_name, buffer_sname, len(players))

    players.append(new_user)
    return new_user.toJSON()





if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=3000)