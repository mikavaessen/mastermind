from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'Start New Game':
            #check for checkbox hard mode
            return render_template('Login.php')
        elif request.form['submit'] == 'Statistics':
            return render_template('Statistics.php')
        elif request.form['Msg'] == 'StartGame':
            #Start new game
            return render_template('Game.php')
        elif request.form['Msg'] == 'CheckResult':
            # check result and redirect to game page or result
            pass
        elif request.form['Msg'] == 'Return':
            return render_template('index.php')
    return render_template('index.php')

if __name__ == '__main__':
    app.run(debug=True)

