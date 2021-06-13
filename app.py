from flask import Flask
from flask import render_template
from flask import request
from backend import GamePlay
from guess import Guess

Game:GamePlay
guesses = list()
colours = list()
names = list()
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index(Game=Game, colours=colours, guesses=guesses, names=names):
    correct = ['Zwart', 'Zwart', 'Zwart', 'Zwart']
    if request.method == 'POST':
        #Go to game settings
        if request.form['Msg'] == 'login':
            return render_template('Login.php')
        #Show statistics
        elif request.form['Msg'] == 'stats':
            names = Game.db.getNames()
            return render_template('Statistics.php', name=names[0], players=names)
        elif request.form['Msg'] == 'statsFilter':
            names = Game.db.getNames()
            return render_template('Statistics.php', name=request.form['name'],  players=names)
        elif request.form['Msg'] == 'StartGame':
            #Start new game after fetching game settings
            guesses = list()
            colourAmount = int(request.form['colours'])
            #tryAmount = int(request.form['tries'])
            tryAmount = 4
            gameMode = request.form['difficulty']
            Game = GamePlay(colourAmount, tryAmount, gameMode)
            inserts = list()
            feedbacks = list()
            for i in range(Game.positionAmount):
                inserts.append(['Empty', 'Empty', 'Empty', 'Empty'])
                feedbacks.append(['Empty', 'Empty', 'Empty', 'Empty'])
            colours = Game.allColours[:colourAmount]
            print(colours)
            return render_template('Game.php', inserts=inserts, feedback=feedbacks, tries=tryAmount, colours=colours)
        elif request.form['Msg'] == 'CheckResult':
            # check result and redirect to game page or result
            print(colours)
            guessNum = int(0)
            guess = list()
            #First colour
            guessNum += colours.index(request.form['colour0']) * 1000
            guess.append(request.form['colour0'])
            #Second colour
            guessNum += colours.index(request.form['colour1']) * 100
            guess.append(request.form['colour0'])
            #Third colour
            guessNum += colours.index(request.form['colour2']) * 10
            guess.append(request.form['colour0'])
            #Fourth colour
            guessNum += colours.index(request.form['colour3'])
            guess.append(request.form['colour0'])
            feedback = list()
            feedback, temp = Game.setGuessedColours(guessNum)
            guesses.append(Guess(guess, feedback))
            if Game.ctr >= Game.positionAmount:
                if feedback == correct:
                    return render_template('Result.php', result=True)
                else:
                    return render_template('Result.php', result=True)
            else:
                if feedback == correct:
                    return render_template('Result.php', result=True)
                else:
                    inserts = []
                    feedbacks = []
                    for g in guesses:
                        inserts.append(g.guesses)
                        feedbacks.append(g.feedback)
                    for i in range(len(guesses), Game.positionAmount):
                        inserts.append(['Empty', 'Empty', 'Empty', 'Empty'])
                        feedbacks.append(['Empty', 'Empty', 'Empty', 'Empty'])
                    return render_template('Game.php', colours=colours, inserts=inserts, feedback=feedbacks, tries=Game.tryAmount)                        
        elif request.form['Msg'] == 'return':
            #Return back to the homepage
            return render_template('index.php')
    return render_template('index.php', inserts='no', tries=4, colours=['Rood', 'Geel', 'Groen'])

if __name__ == '__main__':
    app.run(debug=True)

