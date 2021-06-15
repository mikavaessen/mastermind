from flask import Flask
from flask import render_template
from flask import request
from backend import GamePlay
from Manager import Static
from guess import Guess

Static.Game = GamePlay(6, 4, 'Easy')

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    correct = ['Zwart', 'Zwart', 'Zwart', 'Zwart']
    if request.method == 'POST':
        print(request.form['Msg'])
        #Go to game settings
        if request.form['Msg'] == 'login':
            return render_template('Login.php')
        #Show statistics
        elif request.form['Msg'] == 'stats':
            Static.Players = Static.Game.db.getNames()
            data = Static.Game.db.getPlayerData(Static.Players[0])
            return render_template('Statistics.php', name=Static.Players[0], players=Static.Players, data=data)
        elif request.form['Msg'] == 'statsFilter':
            Static.Players = Static.Game.db.getNames()
            data = Static.Game.db.getPlayerData(request.form['name'])
            return render_template('Statistics.php', name=request.form['name'],  players=Static.Players, data=data)
        elif request.form['Msg'] == 'StartGame':
            #Start new game after fetching game settings
            Static.Guesses = list()
            colourAmount = int(request.form['colours'])
            tryAmount = int(request.form['tries'])
            gameMode = request.form['difficulty']
            Static.Game = GamePlay(colourAmount, tryAmount, gameMode)
            inserts = list()
            feedbacks = list()
            for i in range(Static.Game.positionAmount):
                inserts.append(['Empty', 'Empty', 'Empty', 'Empty'])
                feedbacks.append(['Empty', 'Empty', 'Empty', 'Empty'])
            Static.Colours = Static.Game.allColours[:colourAmount]
            return render_template('Game.php', inserts=inserts, feedback=feedbacks, tries=tryAmount, colours=Static.Colours)
        elif request.form['Msg'] == 'CheckResult':
            # check result and redirect to game page or result
            guessNum = ''
            guess = list()
            #First colour
            guessNum += str(Static.Colours.index(request.form['colour0']) * 1000)[0]
            guess.append(request.form['colour0'])
            #Second colour
            guessNum += str(Static.Colours.index(request.form['colour1']) * 100)[0]
            guess.append(request.form['colour1'])
            #Third colour
            guessNum += str(Static.Colours.index(request.form['colour2']) * 10)[0]
            guess.append(request.form['colour2'])
            #Fourth colour
            guessNum += str(Static.Colours.index(request.form['colour3']))[0]
            guess.append(request.form['colour3'])
            feedback = list()
            feedback, temp = Static.Game.setGuessedColours(guessNum)
            print(guessNum, feedback)
            Static.Guesses.append(Guess(guess, feedback))
            if Static.Game.ctr >= Static.Game.positionAmount:
                if feedback == correct:
                    return render_template('Result.php', result='TRUE')
                else:
                    return render_template('Result.php', result='FALSE')
            else:
                if feedback == correct:
                    return render_template('Result.php', result='TRUE')
                else:
                    inserts = []
                    feedbacks = []
                    for g in Static.Guesses:
                        inserts.append(g.guesses)
                        feedbacks.append(g.feedback)
                    for i in range(len(Static.Guesses), Static.Game.positionAmount):
                        inserts.append(['Empty', 'Empty', 'Empty', 'Empty'])
                        feedbacks.append(['Empty', 'Empty', 'Empty', 'Empty'])
                    return render_template('Game.php', colours=Static.Colours, inserts=inserts, feedback=feedbacks, tries=Static.Game.positionAmount)                        
        elif request.form['Msg'] == 'returnEndGame':
            name = request.form['nickName']
            result = request.form['result']
            if len(name) == 0:
                return render_template('index.php')
            else:
                Static.Game.db.addGame(name, Static.Game.ctr, result, Static.Game.gameMode)
                return render_template('index.php')
        elif request.form['Msg'] == 'return':
            #Return back to the homepage
            return render_template('index.php')
    return render_template('index.php')

if __name__ == '__main__':
    app.run(debug=True)

