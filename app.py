from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from static.Backend.backend import GamePlay

names = ['Select nickname']
app = Flask(__name__)
Game:GamePlay

@app.route('/', methods=['POST', 'GET'])
def index():
    colours = ['green', 'yellow', 'blue', 'red', 'orange'] #need the selected possible colours from the backend 
    colours.insert(0, 'Select a colour')
    if request.method == 'POST':
        #Go to game settings
        if request.form['Msg'] == 'login':
            return render_template('Login.php', names=names)
        #Show statistics
        elif request.form['Msg'] == 'stats':
            return render_template('Statistics.php', name='Mika', players=['Mika', 'Leon', 'Gijs'])
        elif request.form['Msg'] == 'statsFilter':
            return render_template('Statistics.php', name=request.form['name'],  players=['Mika', 'Leon', 'Gijs'])
        elif request.form['Msg'] == 'StartGame':
            #Start new game after fetching game settings
            colourAmount = request.form['colours']
            tryAmount = request.form['tries']
            gameMode = ''
            if request.form.get('hardmode'):
                gameMode = 'hard'
            else:
                gameMode = 'normal'
            #Game = GamePlay(colourAmount, tryAmount, gameMode)
            colours = ['green', 'yellow', 'blue', 'red', 'orange'] #need the selected possible colours from the backend 
            colours.insert(0, 'Select a colour')
            return render_template('Game.php', inserts=None, feedback=None, tries=tryAmount, colours=colours)
        elif request.form['Msg'] == 'CheckResult':
            # check result and redirect to game page or result
            if result == 'wrong':
                return render_template('Result.php', result=False)
            else:
                return render_template('Result.php', result=True)
            pass
        elif request.form['Msg'] == 'AddName':
            #Add a new nickname
            names.append(request.form['NewNameField'])
            return render_template('Login.php', names=names)
        elif request.form['Msg'] == 'return':
            #Return back to the homepage
            return render_template('index.php')
    return render_template('index.php')

if __name__ == '__main__':
    app.run(debug=True)

