from flask import Flask

app = Flask(__name__)

@app.route('/how-are-you')
def haha():
    return 'iam fine!'

@app.route('/')
def main():
    return 'srver works!'


players = ['Вася', 'петя', 'гриша']

@app.route('/users')
def playesr():
    return str(players)

if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=3000)