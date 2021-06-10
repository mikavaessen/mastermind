from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from backend import GamePlay

names = ['Select nickname']
app = Flask(__name__)
Game:GamePlay

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #Go to game settings
        if request.form['Msg'] == 'login':
            return render_template('Login.php', names=names)
        #Show statistics
        elif request.form['Msg'] == 'stats':
            return render_template('Statistics.php')
        elif request.form['Msg'] == 'StartGame':
            #Start new game after 
            colourAmount = request.form['colours']
            tryAmount = request.form['tries']
            gameMode = ''
            if request.form.get('hardmode'):
                gameMode = 'hard'
            else:
                gameMode = 'normal'
            #Game = GamePlay(colourAmount, tryAmount, gameMode)

            return render_template('Game.php', inserts=None, feedback=None)
        elif request.form['Msg'] == 'CheckResult':
            # check result and redirect to game page or result
            if result == 'wrong':
                render_template('Result.php', result=False)
            pass
        elif request.form['Msg'] == 'AddName':
            names.append(request.form['NewNameField'])
            return render_template('Login.php', names=names)
        elif request.form['Msg'] == 'return':
            return render_template('index.php')
    return render_template('Result.php', result=False)

if __name__ == '__main__':
    app.run(debug=True)

